#!/usr/bin/env python3
"""
DOCX Structure Checker
Validates the structure of a .docx manuscript: heading hierarchy, paragraph length,
table formatting, figure references, and style consistency.

Usage:
    python check_docx_structure.py manuscript.docx
    python check_docx_structure.py manuscript.docx --output report.md
"""

import sys
import argparse
from pathlib import Path
from collections import Counter


def check_docx_structure(docx_path: str) -> dict:
    """Check structure of a .docx file."""
    result = {
        'success': False,
        'headings': [],
        'heading_issues': [],
        'paragraph_issues': [],
        'table_issues': [],
        'figure_issues': [],
        'style_issues': [],
        'summary': {}
    }

    try:
        from docx import Document
    except ImportError:
        result['style_issues'].append({
            'type': 'missing_dependency',
            'detail': 'python-docx not installed. Run: pip install python-docx'
        })
        return result

    try:
        doc = Document(docx_path)
    except Exception as e:
        result['style_issues'].append({
            'type': 'read_error',
            'detail': f'Cannot read file: {e}'
        })
        return result

    # 1. Check heading hierarchy
    heading_levels = []
    for para in doc.paragraphs:
        if para.style.name.startswith('Heading'):
            level = int(para.style.name.replace('Heading ', '0'))
            heading_levels.append((level, para.text[:100]))
            result['headings'].append({
                'level': level,
                'text': para.text[:100],
                'style': para.style.name
            })

    # Check heading jumps (e.g., H1 → H3 without H2)
    for i in range(1, len(heading_levels)):
        prev_lvl = heading_levels[i-1][0]
        curr_lvl = heading_levels[i][0]
        if curr_lvl > prev_lvl + 1:
            result['heading_issues'].append({
                'type': 'heading_jump',
                'detail': f'Heading jump: "{heading_levels[i-1][1]}" (H{prev_lvl}) → "{heading_levels[i][1]}" (H{curr_lvl})'
            })

    if not heading_levels:
        result['heading_issues'].append({
            'type': 'no_headings',
            'detail': 'No headings found in document'
        })

    # 2. Check paragraph length
    for i, para in enumerate(doc.paragraphs):
        text = para.text.strip()
        if not text:
            continue
        words = len(text.split())
        if words > 200:
            result['paragraph_issues'].append({
                'type': 'too_long',
                'position': i,
                'detail': f'Paragraph {i}: {words} words (max 200)',
                'preview': text[:100]
            })
        elif words < 10 and para.style.name != 'Heading':
            result['paragraph_issues'].append({
                'type': 'too_short',
                'position': i,
                'detail': f'Paragraph {i}: only {words} words',
                'preview': text[:100]
            })

    # 3. Check tables
    for i, table in enumerate(doc.tables):
        rows = len(table.rows)
        cols = len(table.columns)

        # Check header formatting
        header_cells = table.rows[0].cells
        for cell in header_cells:
            for para in cell.paragraphs:
                for run in para.runs:
                    if run.font.color and run.font.color.rgb:
                        rgb = str(run.font.color.rgb)
                        # Detect dark blue headers
                        if '0000' in rgb and int(rgb[:2], 16) < 50:
                            result['table_issues'].append({
                                'type': 'dark_header',
                                'table': i,
                                'detail': f'Table {i}: dark colored header ({rgb}), use bold text instead'
                            })

        # Check for empty cells
        for r_idx, row in enumerate(table.rows):
            for c_idx, cell in enumerate(row.cells):
                if not cell.text.strip():
                    result['table_issues'].append({
                        'type': 'empty_cell',
                        'table': i,
                        'detail': f'Table {i}: empty cell at row {r_idx}, col {c_idx}'
                    })

    # 4. Check figure/table references
    full_text = '\n'.join(p.text for p in doc.paragraphs)
    figure_captions = re.findall(r'(?:Figure|Fig\.|图)\s*\d+', full_text)
    table_captions = re.findall(r'(?:Table|表)\s*\d+', full_text)

    result['summary'] = {
        'total_paragraphs': len(doc.paragraphs),
        'total_headings': len(heading_levels),
        'total_tables': len(doc.tables),
        'figure_references': len(figure_captions),
        'table_references': len(table_captions),
        'heading_issues': len(result['heading_issues']),
        'paragraph_issues': len(result['paragraph_issues']),
        'table_issues': len(result['table_issues']),
    }

    result['success'] = (
        len(result['heading_issues']) == 0 and
        len(result['table_issues']) == 0
    )

    return result


import re  # needed for the figure/table reference check


def generate_report(result: dict, output_path: str = None):
    """Generate structure report."""
    lines = [
        '# DOCX Structure Report',
        '',
        '## Summary',
        f'| Metric | Value |',
        f'|--------|-------|',
        f'| Paragraphs | {result["summary"].get("total_paragraphs", 0)} |',
        f'| Headings | {result["summary"].get("total_headings", 0)} |',
        f'| Tables | {result["summary"].get("total_tables", 0)} |',
        f'| Figure refs | {result["summary"].get("figure_references", 0)} |',
        f'| Table refs | {result["summary"].get("table_references", 0)} |',
        '',
    ]

    if result['heading_issues']:
        lines.extend(['## Heading Issues', ''])
        for issue in result['heading_issues']:
            lines.append(f'- {issue["detail"]}')
        lines.append('')

    if result['paragraph_issues']:
        lines.extend(['## Paragraph Issues', ''])
        for issue in result['paragraph_issues'][:10]:
            lines.append(f'- {issue["detail"]}')
        if len(result['paragraph_issues']) > 10:
            lines.append(f'- ... and {len(result["paragraph_issues"]) - 10} more')
        lines.append('')

    if result['table_issues']:
        lines.extend(['## Table Issues', ''])
        for issue in result['table_issues']:
            lines.append(f'- {issue["detail"]}')
        lines.append('')

    if result['style_issues']:
        lines.extend(['## Style Issues', ''])
        for issue in result['style_issues']:
            lines.append(f'- {issue["detail"]}')
        lines.append('')

    report = '\n'.join(lines)

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f'Report written to: {output_path}')
    else:
        print(report)


def main():
    parser = argparse.ArgumentParser(
        description='Check DOCX manuscript structure'
    )
    parser.add_argument('docxfile', help='Path to .docx file')
    parser.add_argument('--output', '-o', help='Output report path')

    args = parser.parse_args()

    docx_path = Path(args.docxfile)
    if not docx_path.exists():
        print(f'ERROR: File not found: {args.docxfile}')
        sys.exit(1)

    result = check_docx_structure(str(docx_path))
    generate_report(result, args.output)

    if result['style_issues']:
        for issue in result['style_issues']:
            if issue['type'] == 'missing_dependency':
                print(f'\nTIP: {issue["detail"]}')

    sys.exit(0 if result['success'] else 1)


if __name__ == '__main__':
    main()

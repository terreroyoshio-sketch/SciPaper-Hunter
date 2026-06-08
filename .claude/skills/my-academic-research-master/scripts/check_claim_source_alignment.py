#!/usr/bin/env python3
"""
Claim-Source Alignment Checker
Verifies that each claim/citation in a manuscript is properly supported by its source.
Extracts claims and checks if citations actually support them.

Usage:
    python check_claim_source_alignment.py manuscript.md references.bib
    python check_claim_source_alignment.py manuscript.md --output report.md
"""

import re
import sys
import json
import argparse
from pathlib import Path


def extract_claims_with_citations(text: str) -> list:
    """Extract claims and their associated citations from text."""
    claims = []
    sentences = re.split(r'(?<=[.!?])\s+', text)

    for i, sentence in enumerate(sentences):
        # Find citations in sentence
        cite_pattern = re.findall(r'\\cite(?:t|p|author|year|alt)?\s*\[.*?\]?\s*\{([^}]+)\}', sentence)
        if not cite_pattern:
            cite_pattern = re.findall(r'@(\w[\w:-]*)', sentence)

        if cite_pattern:
            # Flatten multi-citations
            all_keys = []
            for group in cite_pattern:
                keys = [k.strip() for k in group.split(',')]
                all_keys.extend(keys)

            # Extract the claim (remove citation markers)
            claim_text = re.sub(r'\\cite[^}]*\}', '', sentence).strip()
            claim_text = re.sub(r'@\w[\w:-]*', '', claim_text).strip()

            claims.append({
                'sentence_idx': i,
                'claim': claim_text[:200],  # truncate
                'citations': all_keys,
                'full_sentence': sentence.strip()[:300]
            })

    return claims


def check_claim_validity(claims: list) -> list:
    """Check claims for common issues."""
    issues = []
    strong_terms = [
        'prove', 'proves', 'proved', 'demonstrate', 'demonstrates',
        '首次', '第一', '开创', '颠覆', '革命',
        'breakthrough', 'novel', 'first-ever', 'unprecedented',
        '填补空白', '重大突破', '国际领先', '世界领先'
    ]

    for claim in claims:
        text_lower = claim['claim'].lower()
        num_citations = len(claim['citations'])

        # Check: strong claim with weak citation support
        has_strong_term = any(term in text_lower for term in strong_terms)
        if has_strong_term and num_citations < 2:
            issues.append({
                'type': 'strong_claim_weak_support',
                'severity': 'warning',
                'claim': claim['claim'],
                'citations': claim['citations'],
                'detail': f'Strong claim with only {num_citations} citation(s)'
            })

        # Check: no citations
        if num_citations == 0:
            issues.append({
                'type': 'no_citation',
                'severity': 'error',
                'claim': claim['claim'],
                'citations': [],
                'detail': 'Claim has no citation support'
            })

        # Check: "this paper" instead of "this work"
        if 'this paper' in text_lower:
            issues.append({
                'type': 'this_paper',
                'severity': 'info',
                'claim': claim['claim'],
                'citations': claim['citations'],
                'detail': 'Use "this work" instead of "this paper"'
            })

    return issues


def analyze_claim_distribution(claims: list) -> dict:
    """Analyze distribution of citations across claims."""
    all_citations = {}
    for claim in claims:
        for cite in claim['citations']:
            if cite not in all_citations:
                all_citations[cite] = []
            all_citations[cite].append(claim['sentence_idx'])

    return {
        'total_claims': len(claims),
        'total_unique_citations': len(all_citations),
        'citation_frequency': {
            cite: len(idxs) for cite, idxs in
            sorted(all_citations.items(), key=lambda x: -len(x[1]))[:20]
        },
        'uncited_claims': [c for c in claims if not c['citations']],
    }


def main():
    parser = argparse.ArgumentParser(
        description='Check alignment between claims and their citations'
    )
    parser.add_argument('manuscript', help='Path to manuscript (.md or .tex)')
    parser.add_argument('--output', '-o', help='Output report path')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    ms_path = Path(args.manuscript)
    if not ms_path.exists():
        print(f'ERROR: File not found: {args.manuscript}')
        sys.exit(1)

    with open(ms_path, 'r', encoding='utf-8') as f:
        text = f.read()

    print(f'Analyzing: {ms_path}')
    print(f'  Text length: {len(text)} chars')

    claims = extract_claims_with_citations(text)
    print(f'  Claims with citations: {len(claims)}')

    issues = check_claim_validity(claims)
    distribution = analyze_claim_distribution(claims)

    print(f'\n=== Issues Found: {len(issues)} ===')
    errors = [i for i in issues if i['severity'] == 'error']
    warnings = [i for i in issues if i['severity'] == 'warning']
    infos = [i for i in issues if i['severity'] == 'info']
    print(f'  Errors: {len(errors)}')
    print(f'  Warnings: {len(warnings)}')
    print(f'  Info: {len(infos)}')

    for issue in issues[:10]:
        print(f'  [{issue["severity"].upper()}] {issue["detail"][:100]}')

    print(f'\n=== Citation Distribution (top 10) ===')
    for cite, freq in list(distribution['citation_frequency'].items())[:10]:
        print(f'  {cite}: used {freq} times')

    print(f'\n=== Summary ===')
    print(f'  Total claims: {distribution["total_claims"]}')
    print(f'  Unique citations: {distribution["total_unique_citations"]}')
    print(f'  Claims without citations: {len(distribution["uncited_claims"])}')

    if args.json:
        output = {
            'claims': claims,
            'issues': issues,
            'distribution': distribution
        }
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(output, f, indent=2, ensure_ascii=False)
        else:
            print(json.dumps(output, indent=2, ensure_ascii=False))
    elif args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write('# Claim-Source Alignment Report\n\n')
            f.write(f'**File:** {ms_path}\n\n')
            f.write(f'**Total claims:** {distribution["total_claims"]}\n')
            f.write(f'**Issues found:** {len(issues)}\n\n')
            if errors:
                f.write('## Errors\n')
                for e in errors:
                    f.write(f'- {e["detail"]}\n')
            if warnings:
                f.write('## Warnings\n')
                for w in warnings:
                    f.write(f'- {w["detail"]}\n')
        print(f'Report written to: {args.output}')

    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()

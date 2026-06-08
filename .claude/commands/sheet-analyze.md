# /sheet-analyze — 表格分析与统计

## 适用场景
Excel 或 CSV 数据清洗、统计、趋势分析和异常检查。

## 输入要求
- XLSX 或 CSV 文件路径

## 调用模块
`office-productivity-workbench` → `spreadsheet-analysis`

## 工作流
1. 备份原始文件
2. 读取工作表结构
3. 识别字段类型
4. 检查空值、重复、异常值
5. 生成基础描述统计
6. 检查趋势和波动
7. 输出图表建议
8. 不修改原表

## 输出文件
```
outputs/spreadsheet_analysis/
├── data_profile.md
├── anomaly_report.md
├── summary_statistics.csv
├── chart_plan.md
└── cleaned_data.xlsx（如有）
```

## 禁止事项
- 不能擅自删除原始数据
- 不能把异常值直接当错误
- 不能脱离业务解释数字
- 不能编造统计结果
- 对账、财务数据必须保留审计轨迹

## 验收标准
- [ ] 原始文件已备份
- [ ] 异常值已标注
- [ ] 统计结果有业务解释
- [ ] 审计轨迹保留

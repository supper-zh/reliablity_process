# 制程可靠性数据分析系统

## 项目概述
制程可靠性数据分析系统是一个自动化数据处理和分析平台，用于检测远程服务器上的机台数据更新，并将处理后的数据存储到数据库中，同时提供前端界面进行数据查询、可视化和报告生成。

## 功能需求

### 数据类型
1. **HCI&NBTI数据**
   - 检测远程服务器更新
   - 整合CSV和Excel文件到数据库表(UNIFIED_HCI_NBTI_DATA和CSV_DATA)
   - 前端支持筛选查询和Excel导出

2. **VRDB数据**
   - 检测远程服务器更新
   - 批量导入CSV数据到VRDB_DATA表
   - 前端支持筛选查询、散点图展示和数据导出

3. **TDDB数据**
   - 检测远程服务器更新
   - 提取指定字段存入TDDB表
   - 前端支持筛选查询、散点图、Wafer热力图展示和数据导出
   - 支持一键生成标准化Word报告

## 技术架构
- 后端：Python (Flask/FastAPI)
- 数据库：MySQL/PostgreSQL
- 前端：React/Vue.js
- 数据处理：Pandas, NumPy
- 可视化：ECharts/D3.js
- 报告生成：python-docx
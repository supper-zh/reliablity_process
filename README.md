# 制程可靠性数据分析系统

## 项目概述
制程可靠性数据分析系统是一个自动化数据处理和分析平台，用于检测远程服务器上的机台数据更新，并将处理后的数据存储到数据库中，同时提供前端界面进行数据查询、可视化和报告生成。

该系统旨在提高半导体制造过程中数据处理的效率和准确性，通过自动化监控和分析关键可靠性参数，帮助工程师快速识别潜在问题并生成标准化报告。

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
- 后端：Python (Flask)
- 数据库：MySQL
- 前端：HTML/CSS/JavaScript (使用Chart.js进行数据可视化)
- 数据处理：Pandas, NumPy
- 可视化：Chart.js, Matplotlib
- 报告生成：python-docx

## 项目结构
```
project/
├── backend/                 # 后端代码
│   ├── app.py               # Flask应用入口
│   ├── models/              # 数据库模型定义
│   │   ├── hci_nbti_model.py # HCI&NBTI数据模型
│   │   ├── vrdb_model.py     # VRDB数据模型
│   │   └── tddb_model.py     # TDDB数据模型
│   ├── utils/               # 工具类
│   │   ├── data_processor.py # 数据处理工具
│   │   ├── database.py       # 数据库连接工具
│   │   ├── file_monitor.py   # 文件监控工具
│   │   └── report_generator.py # 报告生成工具
│   └── views/               # 视图函数
├── config/                  # 配置文件
│   └── config.py            # 系统配置
├── data/                    # 数据文件
│   └── tddb_data/           # TDDB数据文件
├── frontend/                # 前端代码
│   ├── index.html           # 主页面
│   ├── js/                  # JavaScript文件
│   │   └── main.js          # 主要交互逻辑
│   └── styles/              # 样式文件
│       └── main.css         # 主要样式
├── reports/                 # 生成的报告文件
├── src/                     # 主程序
│   ├── main.py              # 系统主入口
│   ├── check_database.py    # 数据库检查脚本
│   ├── generate_test_data.py # 测试数据生成脚本
│   └── verify_data.py       # 数据验证脚本
├── .env                     # 环境变量配置
├── requirements.txt         # Python依赖包列表
├── README.md                # 项目说明文档
└── 使用文档.md              # 详细使用说明
```

## 环境要求
- Python 3.8+
- MySQL 5.7+
- pip (Python包管理工具)

## 安装指南

### 1. 克隆项目
```bash
git clone <repository-url>
cd process-reliability-analysis-system
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置环境变量
在项目根目录下创建`.env`文件，并配置以下环境变量：
```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=reliability_data
SECRET_KEY=your_secret_key
DEBUG=True
HOST=0.0.0.0
PORT=5000
```

### 4. 初始化数据库
```bash
python src/check_database.py
```

### 5. 生成测试数据（可选）
```bash
python src/generate_test_data.py
```

## 使用说明

### 启动系统
1. 启动后端服务：
   ```bash
   python backend/app.py
   ```

2. 启动文件监控服务：
   ```bash
   python src/main.py
   ```

3. 启动前端服务：
   ```bash
   cd frontend
   python -m http.server 8000
   ```

### 访问系统
打开浏览器访问 `http://localhost:8000`

### 功能使用
1. **数据查询**：在前端界面中使用各类数据查询功能，支持按条件筛选
2. **数据导出**：将查询结果导出为Excel文件
3. **数据可视化**：查看散点图、热力图等可视化图表
4. **报告生成**：在报告生成页面选择报告类型和时间范围，系统将自动生成Word格式的报告文件

## 配置说明

### 数据库配置
在`config/config.py`中配置数据库连接信息：
```python
DATABASE_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'user': os.getenv('DB_USER', 'root'),

    'password': os.getenv('DB_PASSWORD', '123456'),
    'database': os.getenv('DB_NAME', 'reliability_data'),
    'charset': 'utf8mb4'
}
```

### 文件路径配置
```python
FILE_PATHS = {
    'hci_nbti_source': os.getenv('HCI_NBTI_SOURCE_PATH', '/remote/hci_nbti_data'),
    'vrdb_source': os.getenv('VRDB_SOURCE_PATH', '/remote/vrdb_data'),
    'tddb_source': os.getenv('TDDB_SOURCE_PATH', './data/tddb_data'),
    'processed_data': os.getenv('PROCESSED_DATA_PATH', './data/processed'),
    'reports': os.getenv('REPORTS_PATH', './reports')
}
```

## API接口文档

### HCI&NBTI数据接口
- `GET /api/hci-nbti/search` - 查询HCI&NBTI数据
- `GET /api/hci-nbti/export` - 导出HCI&NBTI数据

### VRDB数据接口
- `GET /api/vrdb/search` - 查询VRDB数据
- `GET /api/vrdb/export` - 导出VRDB数据

### TDDB数据接口
- `GET /api/tddb/search` - 查询TDDB数据
- `GET /api/tddb/export` - 导出TDDB数据

### 报告接口
- `POST /api/report/generate` - 生成报告
- `GET /api/report/download/<filename>` - 下载报告

## 数据模型

### HCI&NBTI数据表 (unified_hci_nbti_data)
- id: 主键
- lot_id: 批号
- device_id: 设备ID
- device_name: 设备名称
- std: 标准差
- vtd: 阈值电压退化
- csv_name: CSV文件名
- created_at: 创建时间
- updated_at: 更新时间

### VRDB数据表 (vrdb_data)
- id: 主键
- device_id: 设备ID
- test_date: 测试日期
- voltage: 电压值
- current: 电流值
- resistance: 电阻值
- temperature: 温度
- created_at: 创建时间
- updated_at: 更新时间

### TDDB数据表 (tddb)
- id: 主键
- device_id: 设备ID
- wafer_id: 晶圆ID
- x_coordinate: X坐标
- y_coordinate: Y坐标
- value: 测量值
- test_date: 测试日期
- created_at: 创建时间
- updated_at: 更新时间

## 故障排除

### 数据库连接失败
1. 检查数据库服务是否启动
2. 验证数据库配置是否正确
3. 确认网络连接是否正常

### 数据未处理
1. 检查文件监控服务是否运行
2. 确认源数据文件路径配置是否正确
3. 查看日志文件获取错误信息

### Web服务无法访问
1. 检查后端服务是否启动
2. 确认端口是否被占用
3. 验证防火墙设置

## 贡献指南
1. Fork项目
2. 创建功能分支
3. 提交更改
4. 发起Pull Request

## 许可证
本项目采用MIT许可证，详情请见LICENSE文件。

## 联系方式
如有问题，请联系项目维护者。
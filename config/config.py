"""制程可靠性数据分析系统配置文件
"""

import os

# 数据库配置
DATABASE_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', '123456'),
    'database': os.getenv('DB_NAME', 'reliability_data'),
    'charset': 'utf8mb4'
}

# 文件路径配置
FILE_PATHS = {
    'hci_nbti_source': os.getenv('HCI_NBTI_SOURCE_PATH', '/remote/hci_nbti_data'),
    'vrdb_source': os.getenv('VRDB_SOURCE_PATH', '/remote/vrdb_data'),
    'tddb_source': os.getenv('TDDB_SOURCE_PATH', './data/tddb_data'),
    'processed_data': os.getenv('PROCESSED_DATA_PATH', './data/processed'),
    'reports': os.getenv('REPORTS_PATH', './reports')
}

# 应用配置
APP_CONFIG = {
    'secret_key': os.getenv('SECRET_KEY', 'your-secret-key'),
    'debug': os.getenv('DEBUG', 'False').lower() == 'true',
    'host': os.getenv('HOST', '0.0.0.0'),
    'port': int(os.getenv('PORT', 5000))
}
# 数据库表名配置
TABLE_NAMES = {
    'hci_nbti_unified': 'UNIFIED_HCI_NBTI_DATA',
    'hci_nbti_csv': 'CSV_DATA',
    'vrdb': 'VRDB_DATA',
    'tddb': 'TDDB'
}

# 时间配置
TIME_CONFIG = {
    'file_check_interval': 60  # 文件检查间隔(秒)
}

# 报告配置
REPORT_CONFIG = {
    'report_dir': 'reports'  # 报告存储目录
}

# 其他配置
OTHER_CONFIG = {
    'check_interval': int(os.getenv('CHECK_INTERVAL', 300)),  # 检查间隔(秒)
    'data_retention_days': int(os.getenv('DATA_RETENTION_DAYS', 365))  # 数据保存天数
}
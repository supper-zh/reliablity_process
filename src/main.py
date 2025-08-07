"""制程可靠性数据分析系统主应用
"""

import sys
import os
import time
import threading

# 将项目根目录添加到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.utils.file_monitor import FileMonitor
from backend.utils.data_processor import DataProcessor
from backend.utils.database import init_database


def process_data_updates(updates):
    """处理数据更新
    
    Args:
        updates (dict): 更新信息
    """
    processor = DataProcessor()
    
    # 根据更新类型处理数据
    if updates.get('hci_nbti', False):
        processor.process_hci_nbti_data()
        
    if updates.get('vrdb', False):
        processor.process_vrdb_data()
        
    if updates.get('tddb', False):
        processor.process_tddb_data()


def main():
    """主函数
    """
    print("启动制程可靠性数据分析系统...")
    
    # 初始化数据库
    init_database()
    print("数据库初始化完成")
    
    # 创建文件监控器
    monitor = FileMonitor()
    
    # 启动监控
    monitor.start_monitoring(callback=process_data_updates)


if __name__ == "__main__":
    main()
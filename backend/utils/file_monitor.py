"""文件监控工具
"""

import os
import time
from datetime import datetime
from config.config import FILE_PATHS, TIME_CONFIG


class FileMonitor:
    """文件监控器
    
    用于监控远程服务器上的数据文件夹是否有更新
    """
    
    def __init__(self):
        """初始化文件监控器
        """
        self.last_check_time = datetime.now()
        
    def check_for_updates(self):
        """检查所有数据源文件夹是否有更新
        
        Returns:
            dict: 包含各类数据是否有更新的字典
        """
        updates = {
            'hci_nbti': self._check_hci_nbti_updates(),
            'vrdb': self._check_vrdb_updates(),
            'tddb': self._check_tddb_updates()
        }
        
        self.last_check_time = datetime.now()
        return updates
    
    def _check_hci_nbti_updates(self):
        """检查HCI&NBTI数据是否有更新
        
        Returns:
            bool: 是否有更新
        """
        # 检查HCI和NBTI文件夹
        hci_path = os.path.join(FILE_PATHS['hci_nbti_source'], 'HCI')
        nbti_path = os.path.join(FILE_PATHS['hci_nbti_source'], 'NBTI')
        
        # 这里应该实现具体的文件更新检查逻辑
        # 例如检查文件修改时间或新增文件
        return self._check_directory_updates(hci_path) or self._check_directory_updates(nbti_path)
    
    def _check_vrdb_updates(self):
        """检查VRDB数据是否有更新
        
        Returns:
            bool: 是否有更新
        """
        vrdb_path = FILE_PATHS['vrdb_source']
        return self._check_directory_updates(vrdb_path)
    
    def _check_tddb_updates(self):
        """检查TDDB数据是否有更新
        
        Returns:
            bool: 是否有更新
        """
        tddb_path = FILE_PATHS['tddb_source']
        return self._check_directory_updates(tddb_path)
    
    def _check_directory_updates(self, directory_path):
        """检查指定目录是否有更新
        
        Args:
            directory_path (str): 目录路径
            
        Returns:
            bool: 是否有更新
        """
        # 如果目录不存在，返回False
        if not os.path.exists(directory_path):
            return False
            
        # 获取目录中所有文件的修改时间
        try:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    # 获取文件修改时间
                    mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                    # 如果文件修改时间在上次检查之后，说明有更新
                    if mod_time > self.last_check_time:
                        return True
            return False
        except Exception as e:
            print(f"检查目录更新时出错: {e}")
            return False
    
    def start_monitoring(self, callback=None):
        """开始监控
        
        Args:
            callback (function): 检查到更新时的回调函数
        """
        print("开始监控文件更新...")
        while True:
            updates = self.check_for_updates()
            if any(updates.values()):
                print(f"检测到数据更新: {updates}")
                if callback:
                    callback(updates)
            else:
                print("未检测到数据更新")
            
            # 等待指定时间间隔
            time.sleep(TIME_CONFIG['file_check_interval'])
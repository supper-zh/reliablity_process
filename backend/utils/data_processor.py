"""数据处理工具
"""

import pandas as pd
import os
from datetime import datetime
from backend.utils.database import get_db_session
from backend.models.hci_nbti_model import UnifiedHciNbtiData, CsvData
from backend.models.vrdb_model import VrdbData
from backend.models.tddb_model import TddbData
from config.config import FILE_PATHS


class DataProcessor:
    """数据处理器
    
    用于处理不同类型的数据文件并存储到数据库
    """
    
    def __init__(self):
        """初始化数据处理器
        """
        pass
    
    def process_hci_nbti_data(self):
        """处理HCI&NBTI数据
        
        处理HCI和NBTI文件夹中的数据文件，并存储到UNIFIED_HCI_NBTI_DATA和CSV_DATA表中
        """
        print("开始处理HCI&NBTI数据...")
        
        # 处理HCI数据
        hci_path = os.path.join(FILE_PATHS['hci_nbti_source'], 'HCI')
        self._process_hci_nbti_folder(hci_path)
        
        # 处理NBTI数据
        nbti_path = os.path.join(FILE_PATHS['hci_nbti_source'], 'NBTI')
        self._process_hci_nbti_folder(nbti_path)
        
        print("HCI&NBTI数据处理完成")
    
    def _process_hci_nbti_folder(self, folder_path):
        """处理HCI或NBTI文件夹
        
        Args:
            folder_path (str): 文件夹路径
        """
        if not os.path.exists(folder_path):
            print(f"文件夹不存在: {folder_path}")
            return
            
        # 获取会话
        session = get_db_session()
        
        try:
            # 遍历文件夹中的所有文件
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    
                    # 根据文件扩展名处理
                    if file.endswith('.csv'):
                        self._process_hci_nbti_csv(file_path, session)
                    elif file.endswith('.xlsx') or file.endswith('.xls'):
                        self._process_hci_nbti_excel(file_path, session)
            
            # 提交事务
            session.commit()
        except Exception as e:
            # 回滚事务
            session.rollback()
            print(f"处理HCI&NBTI数据时出错: {e}")
        finally:
            # 关闭会话
            session.close()
    
    def _process_hci_nbti_csv(self, file_path, session):
        """处理HCI&NBTI CSV文件
        
        Args:
            file_path (str): CSV文件路径
            session (Session): 数据库会话
        """
        try:
            # 读取CSV文件
            df = pd.read_csv(file_path)
            
            # 获取文件名
            csv_name = os.path.basename(file_path)
            
            # 处理UNIFIED_HCI_NBTI_DATA表数据
            # 这里需要根据实际CSV文件结构调整
            for index, row in df.iterrows():
                # 创建UnifiedHciNbtiData对象
                unified_data = UnifiedHciNbtiData(
                    lot_id=row.get('Lot_id', ''),
                    device_id=row.get('device_id', ''),
                    device_name=row.get('device_name', ''),
                    std=row.get('std', ''),
                    vtd=row.get('vtd', 0.0),
                    csv_name=csv_name,
                    created_at=datetime.now(),
                    updated_at=datetime.now()
                )
                session.add(unified_data)
            
            # 处理CSV_DATA表数据
            # 这里需要根据实际需求处理CSV数据
            csv_data = CsvData(
                csv_name=csv_name,
                change_range=str(df.describe().to_dict()) if not df.empty else '',
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            session.add(csv_data)
            
            print(f"已处理CSV文件: {file_path}")
        except Exception as e:
            print(f"处理CSV文件时出错 {file_path}: {e}")
    
    def _process_hci_nbti_excel(self, file_path, session):
        """处理HCI&NBTI Excel文件
        
        Args:
            file_path (str): Excel文件路径
            session (Session): 数据库会话
        """
        try:
            # 读取Excel文件
            xls = pd.ExcelFile(file_path)
            
            # 获取文件名
            excel_name = os.path.basename(file_path)
            
            # 处理每个工作表
            for sheet_name in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name=sheet_name)
                
                # 处理UNIFIED_HCI_NBTI_DATA表数据
                for index, row in df.iterrows():
                    # 创建UnifiedHciNbtiData对象
                    unified_data = UnifiedHciNbtiData(
                        lot_id=row.get('Lot_id', ''),
                        device_id=row.get('device_id', ''),
                        device_name=row.get('device_name', ''),
                        std=row.get('std', ''),
                        vtd=row.get('vtd', 0.0),
                        csv_name=f"{excel_name}#{sheet_name}",
                        created_at=datetime.now(),
                        updated_at=datetime.now()
                    )
                    session.add(unified_data)
            
            print(f"已处理Excel文件: {file_path}")
        except Exception as e:
            print(f"处理Excel文件时出错 {file_path}: {e}")
    
    def process_vrdb_data(self):
        """处理VRDB数据
        
        处理VRDB文件夹中的CSV数据文件，并存储到VRDB_DATA表中
        """
        print("开始处理VRDB数据...")
        
        # VRDB数据路径
        vrdb_path = FILE_PATHS['vrdb_source']
        
        if not os.path.exists(vrdb_path):
            print(f"VRDB数据路径不存在: {vrdb_path}")
            return
            
        # 获取会话
        session = get_db_session()
        
        try:
            # 遍历文件夹中的所有CSV文件
            for root, dirs, files in os.walk(vrdb_path):
                for file in files:
                    if file.endswith('.csv'):
                        file_path = os.path.join(root, file)
                        self._process_vrdb_csv(file_path, session)
            
            # 提交事务
            session.commit()
            print("VRDB数据处理完成")
        except Exception as e:
            # 回滚事务
            session.rollback()
            print(f"处理VRDB数据时出错: {e}")
        finally:
            # 关闭会话
            session.close()
    
    def _process_vrdb_csv(self, file_path, session):
        """处理VRDB CSV文件
        
        Args:
            file_path (str): CSV文件路径
            session (Session): 数据库会话
        """
        try:
            # 读取CSV文件
            df = pd.read_csv(file_path)
            
            # 处理VRDB_DATA表数据
            for index, row in df.iterrows():
                # 创建VrdbData对象
                vrdb_data = VrdbData(
                    device_id=row.get('device_id', ''),
                    test_date=datetime.now(),  # 需要从数据中获取实际测试日期
                    voltage=row.get('voltage', 0.0),
                    current=row.get('current', 0.0),
                    resistance=row.get('resistance', 0.0),
                    temperature=row.get('temperature', 0.0),
                    created_at=datetime.now(),
                    updated_at=datetime.now()
                )
                session.add(vrdb_data)
            
            print(f"已处理VRDB CSV文件: {file_path}")
        except Exception as e:
            print(f"处理VRDB CSV文件时出错 {file_path}: {e}")
    
    def process_tddb_data(self):
        """处理TDDB数据
        
        处理TDDB文件夹中的CSV数据文件，并存储到TDDB表中
        """
        print("开始处理TDDB数据...")
        
        # TDDB数据路径
        tddb_path = FILE_PATHS['tddb_source']
        
        if not os.path.exists(tddb_path):
            print(f"TDDB数据路径不存在: {tddb_path}")
            return
            
        # 获取会话
        session = get_db_session()
        
        try:
            # 遍历文件夹中的所有CSV文件
            for root, dirs, files in os.walk(tddb_path):
                for file in files:
                    if file.endswith('.csv'):
                        file_path = os.path.join(root, file)
                        self._process_tddb_csv(file_path, session)
            
            # 提交事务
            session.commit()
            print("TDDB数据处理完成")
        except Exception as e:
            # 回滚事务
            session.rollback()
            print(f"处理TDDB数据时出错: {e}")
        finally:
            # 关闭会话
            session.close()
    
    def _process_tddb_csv(self, file_path, session):
        """处理TDDB CSV文件
        
        Args:
            file_path (str): CSV文件路径
            session (Session): 数据库会话
        """
        try:
            # 读取CSV文件
            df = pd.read_csv(file_path)
            
            # 获取文件名（用于提取wafer_id）
            file_name = os.path.basename(file_path)
            wafer_id = file_name.split('.')[0]  # 假设文件名就是wafer_id
            
            # 处理TDDB表数据
            for index, row in df.iterrows():
                # 创建TddbData对象
                tddb_data = TddbData(
                    device_id=row.get('device_id', ''),
                    wafer_id=wafer_id,
                    x_coordinate=int(row.get('x', 0)),
                    y_coordinate=int(row.get('y', 0)),
                    value=row.get('value', 0.0),
                    test_date=datetime.now(),  # 需要从数据中获取实际测试日期
                    created_at=datetime.now(),
                    updated_at=datetime.now()
                )
                session.add(tddb_data)
            
            print(f"已处理TDDB CSV文件: {file_path}")
        except Exception as e:
            print(f"处理TDDB CSV文件时出错 {file_path}: {e}")
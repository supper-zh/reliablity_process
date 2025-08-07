"""验证数据库中模拟数据的脚本"""

import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.utils.database import get_db_session, init_database
from backend.models.hci_nbti_model import UnifiedHciNbtiData, CsvData
from backend.models.tddb_model import TddbData
from backend.models.vrdb_model import VrdbData

def verify_data():
    """验证数据库中的数据"""
    # 初始化数据库
    init_database()
    
    # 获取数据库会话
    db = get_db_session()
    
    try:
        # 验证HCI/NBTI数据
        hci_nbti_count = db.query(UnifiedHciNbtiData).count()
        print(f"HCI/NBTI数据表中的记录数: {hci_nbti_count}")
        
        # 验证CSV数据
        csv_count = db.query(CsvData).count()
        print(f"CSV数据表中的记录数: {csv_count}")
        
        # 验证TDDB数据
        tddb_count = db.query(TddbData).count()
        print(f"TDDB数据表中的记录数: {tddb_count}")
        
        # 验证VRDB数据
        vrdb_count = db.query(VrdbData).count()
        print(f"VRDB数据表中的记录数: {vrdb_count}")
        
        # 显示一些示例数据
        print("\n示例HCI/NBTI数据:")
        hci_nbti_sample = db.query(UnifiedHciNbtiData).limit(3).all()
        for data in hci_nbti_sample:
            print(f"  ID: {data.id}, Lot ID: {data.lot_id}, Device ID: {data.device_id}")
            
        print("\n示例TDDB数据:")
        tddb_sample = db.query(TddbData).limit(3).all()
        for data in tddb_sample:
            print(f"  ID: {data.id}, Device ID: {data.device_id}, Wafer ID: {data.wafer_id}")
            
    except Exception as e:
        print(f"验证数据时出错: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    verify_data()
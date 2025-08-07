"""生成半导体可靠性测试模拟数据并插入数据库

该脚本用于生成HCI/NBTI、TDDB和VRDB的模拟数据，并将其插入到数据库中用于测试。
"""

import random
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 加载环境变量
from dotenv import load_dotenv
load_dotenv()

from backend.models.hci_nbti_model import UnifiedHciNbtiData, CsvData
from backend.models.tddb_model import TddbData
from backend.models.vrdb_model import VrdbData
from config.config import DATABASE_CONFIG


def generate_hci_nbti_data(session, count=100):
    """生成HCI/NBTI模拟数据
    
    Args:
        session: 数据库会话
        count (int): 生成数据的数量
    """
    print(f"正在生成 {count} 条HCI/NBTI数据...")
    
    devices = [f"Device_{i}" for i in range(1, 21)]
    lots = [f"Lot_{i}" for i in range(1, 11)]
    stds = ["STD001", "STD002", "STD003", None]
    
    for i in range(count):
        data = UnifiedHciNbtiData(
            lot_id=random.choice(lots),
            device_id=random.choice(devices),
            device_name=f"{random.choice(devices)}_Name",
            std=random.choice(stds),
            vtd=round(random.uniform(0.5, 5.0), 4),
            csv_name=f"data_file_{random.randint(1, 100)}.csv",
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        session.add(data)
    
    # 生成CSV数据
    for i in range(20):
        csv_data = CsvData(
            csv_name=f"data_file_{i+1}.csv",
            change_range=f"Range: {random.uniform(0.1, 1.0):.4f} to {random.uniform(1.0, 10.0):.4f}",
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        session.add(csv_data)
    
    session.commit()
    print(f"成功生成 {count} 条HCI/NBTI数据和20条CSV数据")


def generate_tddb_data(session, count=500):
    """生成TDDB模拟数据
    
    Args:
        session: 数据库会话
        count (int): 生成数据的数量
    """
    print(f"正在生成 {count} 条TDDB数据...")
    
    devices = [f"Device_{i}" for i in range(1, 21)]
    wafers = [f"Wafer_{i}" for i in range(1, 6)]
    
    for i in range(count):
        data = TddbData(
            device_id=random.choice(devices),
            wafer_id=random.choice(wafers),
            x_coordinate=random.randint(0, 100),
            y_coordinate=random.randint(0, 100),
            value=round(random.uniform(1.0, 100.0), 4),
            test_date=datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365)),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        session.add(data)
    
    session.commit()
    print(f"成功生成 {count} 条TDDB数据")


def generate_vrdb_data(session, count=200):
    """生成VRDB模拟数据
    
    Args:
        session: 数据库会话
        count (int): 生成数据的数量
    """
    print(f"正在生成 {count} 条VRDB数据...")
    
    devices = [f"Device_{i}" for i in range(1, 21)]
    
    for i in range(count):
        data = VrdbData(
            device_id=random.choice(devices),
            test_date=datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365)),
            voltage=round(random.uniform(0.5, 5.0), 4),
            current=round(random.uniform(0.001, 0.1), 6),
            resistance=round(random.uniform(100, 10000), 2),
            temperature=round(random.uniform(20, 150), 2),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        session.add(data)
    
    session.commit()
    print(f"成功生成 {count} 条VRDB数据")


def main():
    """主函数"""
    print("开始生成模拟数据...")
    
    # 创建数据库引擎
    engine_url = f"mysql+pymysql://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}?charset={DATABASE_CONFIG['charset']}"
    engine = create_engine(engine_url, echo=False)
    
    # 初始化数据库，创建所有表
    from backend.utils.database import init_database
    
    # 初始化数据库
    init_database()
    
    # 创建会话
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    
    try:
        # 生成各类数据
        generate_hci_nbti_data(session, 100)
        generate_tddb_data(session, 500)
        generate_vrdb_data(session, 200)
        
        print("所有模拟数据生成完成！")
    except Exception as e:
        print(f"生成数据时发生错误: {e}")
        session.rollback()
    finally:
        session.close()


if __name__ == "__main__":
    main()
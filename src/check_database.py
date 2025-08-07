"""检查数据库连接和表状态

该脚本用于检查数据库连接是否正常，以及表是否已创建。
"""

import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 加载环境变量
from dotenv import load_dotenv
load_dotenv()

from backend.utils.database import init_database, engine
from sqlalchemy import text


def check_database():
    """检查数据库连接和表状态"""
    print("检查数据库连接...")
    
    try:
        # 测试数据库连接
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("数据库连接成功！")
            
        # 初始化数据库
        print("初始化数据库...")
        init_database()
        print("数据库初始化完成！")
        
        # 检查表是否存在
        print("检查表是否存在...")
        from sqlalchemy import inspect
        inspector = inspect(engine)
        
        # 获取所有表名
        existing_tables = inspector.get_table_names()
        print(f"数据库中存在的表: {existing_tables}")
        
        # 检查特定表是否存在
        expected_tables = ['unified_hci_nbti_data', 'csv_data', 'tddb', 'vrdb_data']
        for table in expected_tables:
            if table in existing_tables:
                print(f"表 {table} 存在")
            else:
                print(f"表 {table} 不存在")
                
    except Exception as e:
        print(f"数据库连接失败: {e}")


def main():
    """主函数"""
    check_database()


if __name__ == "__main__":
    main()
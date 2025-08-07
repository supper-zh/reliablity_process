"""数据库连接和初始化工具
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.config import DATABASE_CONFIG
import os

# 加载环境变量
from dotenv import load_dotenv
load_dotenv()

# 创建数据库引擎
engine_url = f"mysql+pymysql://{os.getenv('DB_USER', DATABASE_CONFIG['user'])}:{os.getenv('DB_PASSWORD', DATABASE_CONFIG['password'])}@{os.getenv('DB_HOST', DATABASE_CONFIG['host'])}:{os.getenv('DB_PORT', DATABASE_CONFIG['port'])}/{os.getenv('DB_NAME', DATABASE_CONFIG['database'])}?charset={DATABASE_CONFIG['charset']}"
engine = create_engine(engine_url, echo=False)

# 创建会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基础类
Base = declarative_base()

# 导出Base类供其他模块使用
__all__ = ['engine', 'SessionLocal', 'Base', 'get_db_session', 'init_database', 'close_database']


def get_db_session():
    """获取数据库会话
    
    Returns:
        Session: 数据库会话对象
    """
    return SessionLocal()


def init_database():
    """初始化数据库，创建所有表
    """
    # 导入所有模型以确保它们被定义
    from backend.models.hci_nbti_model import UnifiedHciNbtiData, CsvData
    from backend.models.vrdb_model import VrdbData
    from backend.models.tddb_model import TddbData
    
    # 创建所有表
    Base.metadata.create_all(bind=engine)
    

def close_database():
    """关闭数据库连接
    """
    engine.dispose()
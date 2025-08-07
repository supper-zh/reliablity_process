"""VRDB数据模型定义
"""

from sqlalchemy import Column, Integer, String, Float, DateTime
from backend.utils.database import Base


class VrdbData(Base):
    """VRDB_DATA表模型
    
    用于存储VRDB数据
    """
    __tablename__ = 'vrdb_data'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 根据VRDB数据特点定义字段
    device_id = Column(String(50), nullable=False)
    test_date = Column(DateTime, nullable=False)
    voltage = Column(Float, nullable=True)
    current = Column(Float, nullable=True)
    resistance = Column(Float, nullable=True)
    temperature = Column(Float, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
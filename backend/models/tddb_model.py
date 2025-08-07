"""TDDB数据模型定义
"""

from sqlalchemy import Column, Integer, String, Float, DateTime
from backend.utils.database import Base


class TddbData(Base):
    """TDDB表模型
    
    用于存储TDDB数据，支持Wafer热力图展示
    """
    __tablename__ = 'tddb'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String(50), nullable=False)
    wafer_id = Column(String(50), nullable=False)
    x_coordinate = Column(Integer, nullable=False)  # X坐标
    y_coordinate = Column(Integer, nullable=False)  # Y坐标
    value = Column(Float, nullable=True)  # 对应的数值
    test_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
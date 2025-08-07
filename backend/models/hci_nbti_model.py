"""HCI&NBTI数据模型定义
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from backend.utils.database import Base


class UnifiedHciNbtiData(Base):
    """UNIFIED_HCI_NBTI_DATA表模型
    
    用于存储整合后的HCI和NBTI数据
    """
    __tablename__ = 'unified_hci_nbti_data'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    lot_id = Column(String(50), nullable=False)
    device_id = Column(String(50), nullable=False)
    device_name = Column(String(100), nullable=True)
    std = Column(String(50), nullable=True)
    vtd = Column(Float, nullable=True)
    csv_name = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    
    
class CsvData(Base):
    """CSV_DATA表模型
    
    用于存储CSV文件中的变化范围数据
    """
    __tablename__ = 'csv_data'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    csv_name = Column(String(255), nullable=False)
    change_range = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
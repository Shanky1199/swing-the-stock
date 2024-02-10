from sqlalchemy import Column, Integer, ForeignKey, Enum, Float, DateTime
from app.models import Base
from datetime import datetime

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    stock_id = Column(Integer, ForeignKey('stocks.id'))
    trade_type = Column(Enum('buy', 'sell', name='trade_types'))
    quantity = Column(Integer)
    trade_price = Column(Float)
    trade_date = Column(DateTime, default=datetime.utcnow)
from sqlalchemy import Column, Integer, ForeignKey, Float
from app.models import Base

class Portfolio(Base):
    __tablename__ = 'portfolios'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    stock_id = Column(Integer, ForeignKey('stocks.id'))
    quantity = Column(Integer)
    average_buy_price = Column(Float)

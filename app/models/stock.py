from sqlalchemy import Column, Integer, String, Float, Date
from models import Base

class Stock(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True)
    symbol = Column(String(10), nullable=False)
    sector = Column(String(50))
    market_cap = Column(Float)
    date = Column(Date, nullable=False)
    open_price = Column(Float, nullable=False)
    high_price = Column(Float, nullable=False)
    low_price = Column(Float, nullable=False)
    close_price = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Stock(symbol={self.symbol}, date={self.date}, close_price={self.close_price})>"

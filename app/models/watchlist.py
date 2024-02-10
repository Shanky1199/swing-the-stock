from sqlalchemy import Column, Integer, ForeignKey
from app.models import Base

class Watchlist(Base):
    __tablename__ = 'watchlists'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    stock_id = Column(Integer, ForeignKey('stocks.id'))

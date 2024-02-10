from sqlalchemy import Column, Integer, ForeignKey, String, Date
from app.models import Base

class Recommendation(Base):
    __tablename__ = 'recommendations'

    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stocks.id'))
    recommendation_date = Column(Date)
    recommendation_type = Column(String(50))
    reason = Column(String)


from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from models import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    premium_member = Column(Boolean, default=False)
    pan_number = Column(String, nullable=False, unique=True)
    balance = Column(Float, default=0.0)
    portfolio_value = Column(Float, default=0.0)
    total_invested = Column(Float, default=0.0)
    total_returns = Column(Float, default=0.0)
    trades = relationship('Trade', backref='user')
    portfolio = relationship('Portfolio', backref='user')
    watchlist = relationship('Watchlist', backref='user')
    
    def create(self):
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy import create_engine

        engine = create_engine('sqlite:///mydatabase.db')  # Replace with your database connection URL
        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(self)
        session.commit()
        session.close()
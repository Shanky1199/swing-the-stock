
from sqlalchemy import Column, Integer, String, Boolean, Float
from models import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)  # Hashed password, store securely
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    premium_member = Column(Boolean, default=False)  # True if the user is a premium member, False otherwise
    accounts = Column(String)  # Store as a JSON string or serialized list
    pan_number = Column(String, nullable=False, unique=True)  # Unique PAN number for each user
    balance = Column(Float, default=0.0)  # User's balance for stock trading
    portfolio_value = Column(Float, default=0.0)  # Total value of user's portfolio
    total_invested = Column(Float, default=0.0)  # Total amount invested in stocks
    total_returns = Column(Float, default=0.0)  # Total returns from stock investments
    
    def create(self):
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy import create_engine

        engine = create_engine('sqlite:///mydatabase.db')  # Replace with your database connection URL
        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(self)
        session.commit()
        session.close()
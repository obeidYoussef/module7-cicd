from app.database import Base
from sqlalchemy import Column, Integer, String, Float

class PredictionsSentiment(Base):
    __tablename__ = "predictions_sentiment"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    prediction = Column(String, index=True)
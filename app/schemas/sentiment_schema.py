from pydantic import BaseModel

class PredictionSentimentSchema(BaseModel):
    
    text: str
    sentiment: str


class PredictionCreateSchema(BaseModel):
    
    text: str

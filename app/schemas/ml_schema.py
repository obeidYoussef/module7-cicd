from pydantic import BaseModel

class PredictRequestSchema(BaseModel):
    """
    Schema for the prediction request.
    """
    input_data: list[float]

class PredictionSchema(BaseModel):
    """
    Schema for the prediction response.
    """
    prediction: float
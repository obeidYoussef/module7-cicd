from fastapi import APIRouter, HTTPException
from app.services.ml_services import train_model, predict
from app.utils.exception import InvalidInputError
from app.utils.logger import get_logger
from app.schemas.ml_schema import PredictRequestSchema, PredictionSchema

logger = get_logger(__name__)

router = APIRouter(prefix="/ml", tags=["ML"])

@router.post("/train")
def train_ml_model():
    """
    Train the machine learning model.
    """
    try:
        train_model()
        return {"message": "Model trained successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/predict", response_model=PredictionSchema)
def get_prediction(request: PredictRequestSchema):
    """
    Get predictions from the machine learning model.
    """
    try:
        prediction = predict([request.input_data])
        return {"prediction": prediction[0]}
    except InvalidInputError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
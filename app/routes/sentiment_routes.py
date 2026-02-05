from fastapi import APIRouter, HTTPException, Depends
from app.services.sentiment_services import predict_sentiment
from app.schemas.sentiment_schema import PredictionCreateSchema, PredictionSentimentSchema
from app.utils.logger import get_logger
from app.dependencies import get_db
from sqlalchemy.orm import Session
from app.models.prediction_model import PredictionsSentiment


logging = get_logger(__name__)

router = APIRouter(prefix="/sentiment", tags=["Sentiment Analysis"])

@router.post("/predict", response_model=PredictionSentimentSchema)
def predict_sentiment_route(request: PredictionCreateSchema, db: Session = Depends(get_db)):
    """
    Endpoint to predict the sentiment of the input text.
    """
    try:
        logging.info(f"Received text for sentiment prediction: {request.text}")
        sentiment = predict_sentiment(request.text)

        db_predict = PredictionsSentiment(text=request.text, prediction=sentiment["label"])
        db.add(db_predict)
        db.commit()
        db.refresh(db_predict)
        logging.info(f"Saved prediction to database with id: {db_predict.id}")
        return PredictionSentimentSchema(text=request.text, sentiment=sentiment['label'])
    except Exception as e:
        logging.error(f"Error predicting sentiment: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/", response_model=list[PredictionSentimentSchema])
def get_all_predictions(db: Session = Depends(get_db)):
    """
    Endpoint to get all predictions.
    """
    predictions = db.query(PredictionsSentiment).all()
    return [PredictionSentimentSchema(text=pred.text, sentiment=pred.prediction) for pred in predictions]
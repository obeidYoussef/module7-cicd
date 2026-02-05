import re
from transformers import pipeline
from app.utils.logger import get_logger
from app.utils.exception import SentimentPipelineError
from app.utils.exception import PredictionError

logger = get_logger(__name__)

try:
    sentiment_pipeline = pipeline("sentiment-analysis")
except Exception as e:
    logger.error(f"Failed to initialize sentiment analysis pipeline: {e}")
    sentiment_pipeline = None
    raise SentimentPipelineError()

def preprocess_text(text: str) -> str:
    """
    Preprocess the input text by stripping whitespace and converting to lowercase.
    """
    text = text.lower().strip()
    # remove special characters if needed
    text = re.sub(r'[^\w\s]', '', text)
    # remove more special characters
    text = re.sub(r'\s+', ' ', text)
    # remove https links
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    return text

def predict_sentiment(text: str) -> dict:
    """
    Predict the sentiment of the input text using the sentiment analysis pipeline.
    """
    if sentiment_pipeline is None:
        raise SentimentPipelineError()
    
    if not text:
        raise ValueError("Input text is empty.")

    preprocessed_text = preprocess_text(text)
    logger.info(f"Preprocessed text: {preprocessed_text}")

    try:
        sentiment = sentiment_pipeline(preprocessed_text)[0]
        logger.info(f"Predicted sentiment: {sentiment}")
    except Exception as e:
        logger.error(f"Failed to predict sentiment: {e}")
        raise PredictionError()
    return sentiment
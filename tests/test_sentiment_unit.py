from app.services.sentiment_services import predict_sentiment

def test_preprocess_positive():
    text = "I love this product!"
    result = predict_sentiment(text)
    assert result['label'] == 'POSITIVE', f"Expected POSITIVE, got {result['label']}"
    assert 0.9 < result['score'] <= 1.0, f"Expected score > 0.9, got {result['score']}"

def test_preprocess_negative():
    text = "I hate this service."
    result = predict_sentiment(text)
    assert result['label'] == 'NEGATIVE', f"Expected NEGATIVE, got {result['label']}"
    assert 0.9 < result['score'] <= 1.0, f"Expected score > 0.9, got {result['score']}"

def test_predict_sentiment():
    # Test with an empty string
    text = ""
    try:
        predict_sentiment(text)
        assert False, "Expected ValueError for empty input text"
    except ValueError as ve:
        assert True, f"Caught expected ValueError: {ve}"
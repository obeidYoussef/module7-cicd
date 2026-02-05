def test_sentiment_api_positive(test_client):
    input_text = "I absolutely love this!"
    response = test_client.post("/sentiment/predict", json={"text": input_text})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    data = response.json()
    assert data['sentiment'] == 'POSITIVE', f"Expected POSITIVE, got {data['label']}"

def test_sentiment_api_negative(test_client):
    input_text = "This is the worst experience ever."
    response = test_client.post("/sentiment/predict", json={"text": input_text})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    data = response.json()
    assert data['sentiment'] == 'NEGATIVE', f"Expected NEGATIVE, got {data['label']}"
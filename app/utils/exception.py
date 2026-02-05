class InvalidInputError(Exception):
    def __init__(self, message="The input provided is invalid."):
        self.message = message
        super().__init__(self.message)

class ItemNotFoundError(Exception):
    def __init__(self, item_id):
        self.message = f"Item with id {item_id} not found."
        super().__init__(self.message)

class SentimentPipelineError(Exception):
    def __init__(self, message="Sentiment analysis pipeline is not initialized."):
        self.message = message
        super().__init__(self.message)

class PredictionError(Exception):
    def __init__(self, message="An error occurred during prediction."):
        self.message = message
        super().__init__(self.message)
from fastapi import FastAPI, HTTPException
from app.utils.exception import InvalidInputError
from app.utils.logger import get_logger
from app.routes.crud_routes import router as crud_router
from app.routes.ml_routes import router as ml_router
from app.database import Base, engine
from app.routes.sentiment_routes import router as sentiment_router

logger = get_logger(__name__)
logger.info("Starting the ML application")

app = FastAPI(title="ML Prediction API")
app.include_router(crud_router)
app.include_router(ml_router)
app.include_router(sentiment_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "API is running"}


@app.get("/healthcheck")
def root():
    return {"status": "health is good"}


@app.post("/name")
def get_name(name: str):
    if not name:
        raise HTTPException(status_code=400, detail="Name parameter is required")
    return {"message": f"Hello, {name}!"}
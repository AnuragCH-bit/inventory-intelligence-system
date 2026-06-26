from pydantic import BaseModel


class StockPredictionRequest(BaseModel):

    weekly_consumption_velocity: float

    days_of_supply: float

    annual_consumption_value: float

    current_stock: int


class StockPredictionResponse(BaseModel):

    prediction: int

    risk: str

    confidence: str

    recommendation: str
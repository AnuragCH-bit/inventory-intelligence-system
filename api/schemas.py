from pydantic import BaseModel


class StockPredictionRequest(BaseModel):

    weekly_consumption_velocity: float
    days_of_supply: float
    annual_consumption_value: float
    current_stock: int


class StockPredictionResponse(BaseModel):

    prediction: int
    risk: str
    confidence: float
    recommendation: str


class ProcurementRequest(BaseModel):

    sku: str
    question: str


# ----------------------------
# Structured Output Model
# ----------------------------

class ProcurementResult(BaseModel):

    recommendation: str

    priority: str

    confidence: str

    reason: str

    next_action: str


class ProcurementResponse(BaseModel):

    success: bool

    sku: str | None = None

    question: str | None = None

    result: ProcurementResult | None = None

    message: str | None = None
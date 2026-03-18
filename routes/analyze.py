from fastapi import APIRouter, Depends
from services.data_fetcher import get_market_data
from services.ai_analyzer import analyze_data
from utils.auth import verify_token
from utils.rate_limiter import check_limit

router = APIRouter()

@router.get("/analyze/{sector}")
async def analyze_sector(sector: str, token: str = Depends(verify_token)):

    if not check_limit(token):
        return {"error": "Rate limit exceeded"}

    data = get_market_data(sector)
    report = analyze_data(sector, data)

    return {"report": report}
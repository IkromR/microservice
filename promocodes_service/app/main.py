from fastapi import FastAPI, HTTPException
from app.Loyalty import Loyalty


loyaltyList: list[Loyalty] = [
    Loyalty(0, "30% Скидка на бытовую технику"),
    Loyalty(1, "%15 Скидка на электронику"),
    Loyalty(2, "Скидка %10 на продуктовые товары")
]

app = FastAPI()


@app.get("/v1/loyalty")
async def get_loyalty():
    return loyaltyList


@app.get("/v1/loyalty/{id}")
async def get_loyalty_by_id(id: int):
    result = [item for item in loyaltyList if item.id == id]
    if len(result) > 0:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail="Loyalty not found")


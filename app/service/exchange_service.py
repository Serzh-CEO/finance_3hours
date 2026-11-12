from decimal import Decimal
from app.currency_enum import CurrencyEnum
import httpx

async def convert(from_currency: CurrencyEnum,to_currency: CurrencyEnum,amount: Decimal) -> Decimal:
    async with httpx.AsyncClient() as client:
        response = await client.get(
        "https://kurs24.kz/api/convert",
        params={
            "from": from_currency,
            "to": to_currency,
            "amount": amount
        }
    )

    data = response.json()
    return Decimal(data["result"])

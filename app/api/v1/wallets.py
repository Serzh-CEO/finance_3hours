from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.currency_enum import CurrencyEnum
from app.dependency import get_db, get_current_user
from app.models import User
from app.service import wallets as wallets_service
from app.schemas import CreateWalletRequest, WalletResponse

router = APIRouter()

@router.get("/wallet_balance")
def get_wallet_balance(wallet_name: str, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    return wallets_service.get_wallet_balance(db,current_user,wallet_name)


@router.get("/total_balance")
async def get_total_balance(db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user),target_currency=CurrencyEnum.KZT):
    return await wallets_service.get_total_wallet(db,current_user,target_currency=target_currency)

@router.post("/wallets",response_model=WalletResponse)
def create_wallet(wallet: CreateWalletRequest, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    return wallets_service.create_wallet(db,current_user,wallet)


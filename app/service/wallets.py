from decimal import Decimal

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.currency_enum import CurrencyEnum
from app.repository import wallets as wallets_repository
from app.models import User
from app.schemas import CreateWalletRequest, WalletResponse
from app.service.exchange_service import convert


def get_wallet_balance(db: Session , current_user: User,wallet_name: str):
    if not wallets_repository.is_wallet_exist(db,current_user.id,wallet_name):
        raise HTTPException(status_code = 404,detail = f"Wallet '{wallet_name}' not found")

    wallet = wallets_repository.get_wallet_balance_by_name(db,current_user.id,wallet_name)
    return {"wallet": wallet.name , "balance": wallet.balance}


async def get_total_wallet(db: Session , current_user: User, target_currency):
    wallets = wallets_repository.get_all_wallets(db, current_user.id)
    total_balance = Decimal(0)
    for w in wallets:
        target_balance = w.balance
        if w.currency != target_currency:
            target_balance = await convert(w.currency,target_currency,w.balance)
        total_balance+=target_balance
    return total_balance




def create_wallet(db: Session ,current_user: User,wallet: CreateWalletRequest) -> WalletResponse:
    if wallets_repository.is_wallet_exist(db,current_user.id,wallet.name):
        raise HTTPException(
            status_code=400,
            detail= f"Wallet '{wallet.name}' already exists"
        )

    wallet = wallets_repository.create_wallet(db,current_user.id,wallet.name,wallet.initial_balance,wallet.currency)
    db.commit()
    return WalletResponse.model_validate(wallet)

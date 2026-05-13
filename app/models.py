from pydantic import BaseModel


class PlayerActivity(BaseModel):
    player_id: str
    ip_address: str
    device_id: str
    payment_method: str
    bonus_claims: int
    deposits: int
    total_bets: int
    session_minutes: int
    withdrawals: int

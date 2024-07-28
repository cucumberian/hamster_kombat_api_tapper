from pydantic import BaseModel, Field
import time

url = "https://api.hamsterkombatgame.io/clicker/buy-upgrade"


class BuyUpgrade(BaseModel):
    upgradeId: str
    timestamp: int = Field(
        ge=0,
        default_factory=lambda: int(time.time() * 1000),
    )

from pydantic import BaseModel
from pydantic import Field
import datetime


class ClickerUser(BaseModel):
    id: int
    totalCoins: float
    balanceCoins: float
    level: int
    availableTaps: int = Field(ge=0)
    lastSyncUpdate: int = Field(ge=0)
    exchangeId: str
    referralsCount: int
    maxTaps: int
    earnPerTap: int
    earnPassivePerSec: float
    earnPassivePerHour: float
    lastPassiveEarn: float
    tapsRecoverPerSec: float
    createdAt: datetime.datetime
    claimedCipherAt: datetime.datetime
    claimedUpgradeComboAt: datetime.datetime


class TapResponse(BaseModel):
    clickerUser: ClickerUser

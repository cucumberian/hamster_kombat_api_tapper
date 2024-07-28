import time
from pydantic import BaseModel
from pydantic import Field


class Tap(BaseModel):
    count: int = Field(ge=0)
    availableTaps: int = Field(ge=0)
    timestamp: int = Field(
        ge=0,
        default_factory=lambda: int(time.time()),
    )

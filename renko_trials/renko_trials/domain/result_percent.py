import dataclasses
from datetime import datetime


@dataclasses.dataclass
class ResultPercent:
    symbol: str
    percent: float
    score: float
    start_date: datetime
    end_date: datetime

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)

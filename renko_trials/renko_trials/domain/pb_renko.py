import dataclasses
from typing import List
from renko_trials.domain.brick import Brick


@dataclasses.dataclass
class PBRenko:
    bricks: List[Brick]
    percent: float
    number_of_leaks: int

    @classmethod
    def from_dict(cls, d):
        _bricks = [Brick.from_dict(y) for y in d.get("bricks")]
        _percent = int(d.get("percent"))
        _number_of_leaks = float(d.get("number_of_leaks"))
        return PBRenko(_bricks, _percent, _number_of_leaks)

    def to_dict(self):
        return dataclasses.asdict(self)

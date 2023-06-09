import dataclasses


@dataclasses.dataclass
class Brick:
    type: str
    open: float
    close: float
    low: float
    high: float

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)

import json
from renko_trials.domain.brick import Brick


class PBRenkoJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "bricks": [Brick.to_dict(y) for y in o.bricks],
                "percent": o.percent,
                "number_of_leaks": o.number_of_leaks,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)

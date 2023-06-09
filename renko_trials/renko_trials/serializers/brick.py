import json


class BrickJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "type": o.type,
                "open": o.open,
                "close": o.close,
                "low": o.low,
                "high": o.high,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)

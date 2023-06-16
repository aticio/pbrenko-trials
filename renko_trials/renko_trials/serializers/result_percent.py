import json


class ResultPercentJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "symbol": o.symbol,
                "percent": o.percent,
                "score": o.score,
                "start_date": o.start_date.strftime("%Y-%m-%d %H:%M:%S"),
                "end_date": o.end_date.strftime("%Y-%m-%d %H:%M:%S"),
            }
            return to_serialize
        except AttributeError:
            return super().default(o)

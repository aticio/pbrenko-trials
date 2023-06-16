import json

from renko_trials.serializers.result_percent import ResultPercentJsonEncoder
from renko_trials.domain.result_percent import ResultPercent

from datetime import datetime


def test_serialize_domain_result_percent():
    result_percent = ResultPercent(
        symbol="BTCUSDT",
        percent=2.6,
        score=4.2,
        start_date=datetime(2022, 1, 1, 0, 0, 0),
        end_date=datetime(2023, 1, 1, 0, 0, 0)
    )

    expected_json = '''
        {
            "symbol": "BTCUSDT",
            "percent": 2.6,
            "score": 4.2,
            "start_date": "2022-01-01 00:00:00",
            "end_date": "2023-01-01 00:00:00"
        }
    '''

    json_result_percent = json.dumps(result_percent, cls=ResultPercentJsonEncoder)

    assert json.loads(json_result_percent) == json.loads(expected_json)

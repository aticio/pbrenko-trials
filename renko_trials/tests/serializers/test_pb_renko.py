import json

from renko_trials.serializers.pb_renko import PBRenkoJsonEncoder
from renko_trials.domain.pb_renko import PBRenko
from renko_trials.domain.brick import Brick


def test_serialize_domain_pb_renko():
    brick_1 = Brick(
        type="up",
        open=100,
        close=110,
        high=110,
        low=100,
    )

    brick_2 = Brick(
        type="up",
        open=110,
        close=121,
        high=125,
        low=110,
    )

    brick_3 = Brick(
        type="up",
        open=121,
        close=133.1,
        high=133.1,
        low=121,
    )

    brick_4 = Brick(
        type="up",
        open=133.1,
        close=146.1,
        high=150,
        low=133.1,
    )

    brick_5 = Brick(
        type="down",
        open=131.769,
        close=118.5921,
        high=140,
        low=118.5921,
    )

    brick_6 = Brick(
        type="down",
        open=118.5921,
        close=106.73289,
        high=118.5921,
        low=105,
    )

    brick_7 = Brick(
        type="up",
        open=117.406179,
        close=129.1467969,
        high=135,
        low=117.406179,
    )

    brick_8 = Brick(
        type="up",
        open=129.1467969,
        close=142.06147659,
        high=145,
        low=129.1467969,
    )

    pb_renko = PBRenko(
        symbol="BTCUSDT",
        bricks=[brick_1, brick_2, brick_3, brick_4, brick_5, brick_6, brick_7, brick_8],
        percent=10,
        number_of_leaks=5,
    )

    expected_json = '''
        {
            "symbol": "BTCUSDT",
            "bricks": [
                {
                    "type": "up",
                    "open": 100,
                    "close": 110,
                    "high": 110,
                    "low": 100
                },
                {
                    "type": "up",
                    "open": 110,
                    "close": 121,
                    "high": 125,
                    "low": 110
                },
                {
                    "type": "up",
                    "open": 121,
                    "close": 133.1,
                    "high": 133.1,
                    "low": 121
                },
                {
                    "type": "up",
                    "open": 133.1,
                    "close": 146.1,
                    "high": 150,
                    "low": 133.1
                },
                {
                    "type": "down",
                    "open": 131.769,
                    "close": 118.5921,
                    "high": 140,
                    "low": 118.5921
                },
                {
                    "type": "down",
                    "open": 118.5921,
                    "close": 106.73289,
                    "high": 118.5921,
                    "low": 105
                },
                {
                    "type": "up",
                    "open": 117.406179,
                    "close": 129.1467969,
                    "high": 135,
                    "low": 117.406179
                },
                {
                    "type": "up",
                    "open": 129.1467969,
                    "close": 142.06147659,
                    "high": 145,
                    "low": 129.1467969
                }
            ],
            "percent": 10,
            "number_of_leaks": 5
        }
    '''

    json_pb_renko = json.dumps(pb_renko, cls=PBRenkoJsonEncoder)
    assert json.loads(json_pb_renko) == json.loads(expected_json)

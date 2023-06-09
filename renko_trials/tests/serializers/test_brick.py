import json

from renko_trials.serializers.brick import BrickJsonEncoder
from renko_trials.domain.brick import Brick


def test_serialize_domain_brick():
    brick = Brick(
        type="up",
        open=100,
        close=200,
        low=10,
        high=230,
    )

    expected_json = '''
        {
            "type": "up",
            "open": 100,
            "close": 200,
            "low": 10,
            "high": 230
        }
    '''

    json_brick = json.dumps(brick, cls=BrickJsonEncoder)

    assert json.loads(json_brick) == json.loads(expected_json)

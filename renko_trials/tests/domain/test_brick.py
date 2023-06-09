from renko_trials.domain.brick import Brick


def test_brick_model_init():
    brick = Brick(
        type="up",
        open=100,
        close=200,
        low=None,
        high=230,
    )

    assert brick.type == "up"
    assert brick.open == 100
    assert brick.close == 200
    assert brick.low is None
    assert brick.high == 230


def test_brick_model_from_dict():
    init_dict = {
        "type": "up",
        "open": 100,
        "close": 200,
        "low": None,
        "high": 230,
    }

    brick = Brick.from_dict(init_dict)

    assert brick.type == "up"
    assert brick.open == 100
    assert brick.close == 200
    assert brick.low is None
    assert brick.high == 230


def test_brick_model_to_dict():
    init_dict = {
        "type": "up",
        "open": 100,
        "close": 200,
        "low": None,
        "high": 230,
    }

    brick = Brick.from_dict(init_dict)

    assert brick.to_dict() == init_dict

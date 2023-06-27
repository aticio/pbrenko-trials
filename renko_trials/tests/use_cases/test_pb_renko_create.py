import pytest

from unittest import mock
from renko_trials.domain.brick import Brick
from renko_trials.domain.pb_renko import PBRenko
from renko_trials.use_cases.pb_renko_create import PBRenkoCreateUseCase
from renko_trials.requests.pb_renko_create import build_pb_renko_create_request


@pytest.fixture
def market_data():
    return [100, 110, 125, 130, 150, 140, 120, 110, 105, 115, 135, 145]


def test_pb_renko_create(market_data):
    symbol = "BTCUSDT"
    percent = 10
    repo = mock.Mock()
    repo.get_data.return_value = market_data

    request = build_pb_renko_create_request({"symbol": "BTCUSDT", "percent": 6.3, "repo": "crypto"})

    pb_renko_create_use_case = PBRenkoCreateUseCase(repo)
    response = pb_renko_create_use_case.create_pbrenko(request)

    brick_0 = Brick(
        type="first",
        open=100,
        close=100,
        high=100,
        low=100,
    )

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
        high=121,
        low=110,
    )

    brick_3 = Brick(
        type="up",
        open=121,
        close=133.5,
        high=133.5,
        low=121,
    )

    brick_4 = Brick(
        type="up",
        open=133.5,
        close=146,
        high=146,
        low=133.5,
    )

    brick_5 = Brick(
        type="down",
        open=133.5,
        close=118.5,
        high=133.5,
        low=118.5,
    )

    brick_6 = Brick(
        type="down",
        open=118.5,
        close=107.5,
        high=118.5,
        low=107.5,
    )

    brick_7 = Brick(
        type="up",
        open=118.5,
        close=129,
        high=129,
        low=118.5,
    )

    brick_8 = Brick(
        type="up",
        open=129,
        close=142.5,
        high=142.5,
        low=129,
    )

    bricks = [brick_0, brick_1, brick_2, brick_3, brick_4, brick_5, brick_6, brick_7, brick_8]

    pb_renko = PBRenko(
        symbol=symbol,
        bricks=bricks,
        percent=percent,
        number_of_leaks=0,
    )

    assert bool(response) is True
    repo.get_data.assert_called_with()
    assert response.value == pb_renko

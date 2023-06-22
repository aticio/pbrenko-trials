import pytest

from unittest import mock
from renko_trials.domain.brick import Brick


@pytest.fixture
def market_data():
    return [100, 110, 125, 130, 150, 140, 120, 110, 105, 115, 135, 145]


def test_create_percent_based_renko_chart(market_data):
    repo = mock.Mock()
    repo.get_data.return_value = market_data

    result = percent_based_renko_use_case(repo)

    brick_1 = Brick(
        type="up",
        open=100,
        close=100,
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

    bricks = [brick_1, brick_2, brick_3, brick_4, brick_5, brick_6, brick_7, brick_8]

    repo.get_data.assert_called_with()
    assert result == bricks

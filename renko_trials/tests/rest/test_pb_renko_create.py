import json
from unittest import mock

from renko_trials.domain.pb_renko import PBRenko


init_dict = {
        "symbol": "BTCUSDT",
        "bricks": [
            {
                "type": "up",
                "open": 100,
                "close": 110,
                "high": 110,
                "low": 100,
            },
            {
                "type": "up",
                "open": 110,
                "close": 121,
                "high": 125,
                "low": 110,
            },
            {
                "type": "up",
                "open": 121,
                "close": 133.1,
                "high": 133.1,
                "low": 121,
            },
            {
                "type": "up",
                "open": 133.1,
                "close": 146.1,
                "high": 150,
                "low": 133.1,
            },
            {
                "type": "down",
                "open": 131.769,
                "close": 118.5921,
                "high": 140,
                "low": 118.5921,
            },
            {
                "type": "down",
                "open": 118.5921,
                "close": 106.73289,
                "high": 118.5921,
                "low": 105,
            },
            {
                "type": "up",
                "open": 117.406179,
                "close": 129.1467969,
                "high": 135,
                "low": 117.406179,
            },
            {
                "type": "up",
                "open": 129.1467969,
                "close": 142.06147659,
                "high": 145,
                "low": 129.1467969,
            },
        ],
        "percent": 10,
        "number_of_leaks": 5,
    }

pb_renko = PBRenko.from_dict(init_dict)


@mock.patch("application.rest.pb_renko_create.PBRenkoCreateUseCase.create_pbrenko")
def test_create(mock_use_case, client):
    mock_use_case.return_value = pb_renko

    http_response = client.get(
        "/pb_renko_create?symbol=BTCUSDT&percent=6.3"
    )

    assert json.loads(http_response.data.decode("UTF-8")) == init_dict

    mock_use_case.assert_called()
    args, kwargs = mock_use_case.call_args
    assert args[0] == "BTCUSDT"
    assert args[1] == 6.3
    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"

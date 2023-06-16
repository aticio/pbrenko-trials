from renko_trials.domain.result_percent import ResultPercent

from datetime import datetime


def test_result_percent_model_init():
    result_percent = ResultPercent(
        symbol="BTCUSDT",
        percent=2.6,
        score=4.2,
        start_date=datetime(2022, 1, 1, 0, 0, 0),
        end_date=datetime(2023, 1, 1, 0, 0, 0)
    )

    assert result_percent.symbol == "BTCUSDT"
    assert result_percent.percent == 2.6
    assert result_percent.score == 4.2
    assert result_percent.start_date == datetime(2022, 1, 1, 0, 0, 0)
    assert result_percent.end_date == datetime(2023, 1, 1, 0, 0, 0)


def test_result_percent_model_from_dict():
    init_dict = {
        "symbol": "BTCUSDT",
        "percent": 2.6,
        "score": 4.2,
        "start_date": datetime(2022, 1, 1, 0, 0, 0),
        "end_date": datetime(2023, 1, 1, 0, 0, 0)
    }

    result_percent = ResultPercent.from_dict(init_dict)

    assert result_percent.symbol == "BTCUSDT"
    assert result_percent.percent == 2.6
    assert result_percent.score == 4.2
    assert result_percent.start_date == datetime(2022, 1, 1, 0, 0, 0)
    assert result_percent.end_date == datetime(2023, 1, 1, 0, 0, 0)


def test_result_percent_model_to_dict():
    init_dict = {
        "symbol": "BTCUSDT",
        "percent": 2.6,
        "score": 4.2,
        "start_date": datetime(2022, 1, 1, 0, 0, 0),
        "end_date": datetime(2023, 1, 1, 0, 0, 0)
    }

    result_percent = ResultPercent.from_dict(init_dict)

    assert result_percent.to_dict() == init_dict

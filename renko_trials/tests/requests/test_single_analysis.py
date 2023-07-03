from renko_trials.requests.single_analysis import build_single_analysis_request


# incorrect parameter keys
def test_single_analysis_incorrect_parameter_keys():
    symbol = "BTCUSDT"
    percent = 6.3
    start_date = "202101010000"
    end_date = "202301010000"
    repo_param = "crypto"

    # Parameter with typo
    request = build_single_analysis_request({"sybol": symbol, "percent": percent, "repo": repo_param, "start_date": start_date, "end_date": end_date})

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "sybol"
    assert bool(request) is False


# missing parameter
def test_build_single_analysis_request_with_incorrect_number_of_params():
    symbol = "BTCUSDT"
    percent = 6.3
    start_date = "202101010000"
    end_date = "202301010000"

    request = build_single_analysis_request(parameters={"symbol": symbol, "percent": percent, "start_date": start_date, "end_date": end_date})

    assert request.has_errors()
    assert request.errors[0]["message"] == "missing parameter"
    assert bool(request) is False


# invalid parameters
def test_build_single_analysis_request_with_invalid_params():
    # Passing wrong type of object
    request = build_single_analysis_request(parameters=5)

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "parameters"
    assert bool(request) is False

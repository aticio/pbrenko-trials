from renko_trials.requests.pb_renko_create import build_pb_renko_create_request


def test_build_pb_renko_create_request_without_parameters():
    request = build_pb_renko_create_request()

    assert request.has_errors()
    assert bool(request) is False


def test_build_pb_renko_create_request_with_invalid_params():
    # Passing wrong type of object
    request = build_pb_renko_create_request(parameters=5)

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "parameters"
    assert bool(request) is False


def test_build_pb_renko_create_request_with_incorrect_param_keys():
    # Parameter with typo
    request = build_pb_renko_create_request(parameters={"sybol": "BTCUSDT", "percent": 6.3})

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "parameters"
    assert bool(request) is False


def test_build_pb_renko_create_request_with_incorrect_number_of_params():
    request = build_pb_renko_create_request(parameters={"symbol": "BTCUSDT", "percent": 6.3, "repo": "crypto", "wrong_key": "wrong_value"})

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "parameters"
    assert bool(request) is False

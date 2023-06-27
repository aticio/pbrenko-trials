import pytest
from renko_trials.requests.pb_renko_create import build_pb_renko_create_request


def test_build_pb_renko_create_request_without_parameters():
    request = build_pb_renko_create_request()

    assert request.has_errors()
    assert bool(request) is False


# def test_build_pb_renko_create_request_from_empty_dict():
#     request = build_pb_renko_create_request({})

#     assert request.params == {}
#     assert bool(request) is True


def test_build_pb_renko_create_request_with_invalid_params():
    request = build_pb_renko_create_request(parameters=5)

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "parameters"
    assert bool(request) is False


def test_build_pb_renko_create_request_with_incorrect_param_keys():
    request = build_pb_renko_create_request(parameters={"a": 1})

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "parameters"
    assert bool(request) is False


@pytest.mark.parametrize(
    "key", ["symbol", "percent", "repo"]
)
def test_build_pb_renko_create_request_accepted_paramters(key):
    parameters = {key: 1}

    request = build_pb_renko_create_request(parameters=parameters)

    assert request.parameters == parameters
    assert bool(request) is True


@pytest.mark.parametrize("key", ["err_param"])
def test_build_pb_renko_create_request_rejected_params(key):
    params = {key: 1}

    request = build_pb_renko_create_request(parameters=params)

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "parameters"
    assert bool(request) is False

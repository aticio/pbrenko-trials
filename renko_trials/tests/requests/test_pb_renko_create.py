from renko_trials.requests.pb_renko_create import PBRenkoCreateRequest


def test_build_pb_renko_create_request_without_parameters():
    request = PBRenkoCreateRequest()
    assert bool(request) is True


def test_build_pb_renko_create_request_from_empty_dict():
    request = PBRenkoCreateRequest.from_dict({})

    assert bool(request) is True

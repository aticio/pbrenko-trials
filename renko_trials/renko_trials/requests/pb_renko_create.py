class PBRenkoCreateInvalidRequest:
    def __init__(self):
        self.errors = []

    def add_error(self, param, message):
        self.errors.append({"parameter": param, "message": message})

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False


class PBRenkoCreateValidRequest:
    def __init__(self, parameters=None):
        self.parameters = parameters

    def __bool__(self):
        return True


def build_pb_renko_create_request(parameters=None):
    accepted_parameters = ["symbol", "percent", "repo"]
    invalid_req = PBRenkoCreateInvalidRequest()

    if parameters is not None:
        if not isinstance(parameters, dict):
            invalid_req.add_error("parameters", "Is not iterable")
            return invalid_req

        if len(parameters) != 3:
            invalid_req.add_error("parameters", "Wrong number of parameters")
            for key, value in parameters.items():
                if key not in accepted_parameters:
                    invalid_req.add_error("parameters", "Key {} cannot be used".format(key))

        if invalid_req.has_errors():
            return invalid_req
    else:
        invalid_req.add_error("", "Needs 3 parameters, got 0")
        return invalid_req

    return PBRenkoCreateValidRequest(parameters=parameters)

from .api_client import ApiClient


class _FakeResponse:
    def __init__(self, data):
        self.data = data


def deserialize(data, klass):
    return ApiClient().deserialize(_FakeResponse(data), klass)

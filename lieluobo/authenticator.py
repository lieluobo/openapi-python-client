import time
import hmac
import hashlib
from collections import defaultdict


class ApiKeyAuthenticator:
    def __init__(self, secret_id, secret_key):
        self.secret_id = secret_id
        self.secret_key = secret_key

    @staticmethod
    def _make_key_value_list(query_params):
        key_list = []
        value_list = []
        if query_params is not None:
            params = defaultdict(list)
            for k, v in query_params:
                params[str(k)].append(str(v))
            key_list = sorted(params.keys())
            for k in key_list:
                value_list.extend(sorted(params[k]))
        return ','.join(key_list), ','.join(value_list)

    @staticmethod
    def _make_digest(timestamp, method, path, query_params):
        key_list, value_list = ApiKeyAuthenticator._make_key_value_list(query_params)
        message = ";".join([timestamp, method.upper(), path, key_list, value_list]).encode()
        return hashlib.sha512(message).hexdigest().encode()

    def __call__(self, method, path, header_params, query_params):
        timestamp = str(time.time_ns() // 1_000_000)
        digest = self._make_digest(timestamp, method, path, query_params)
        signature = hmac.new(self.secret_key.encode(), digest, hashlib.sha512).hexdigest()
        token = '&'.join([
            'timestamp={}'.format(timestamp),
            'ak={}'.format(self.secret_id),
            'signature={}'.format(signature)
        ])
        header_params['Authorization'] = 'ApiKey {}'.format(token)

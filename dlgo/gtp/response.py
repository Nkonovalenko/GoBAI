__all__ = [
    'Response',
    'error',
    'serialize',
    'success',
]

class Response:
    def __init__(self, status, body):
        self.success = status
        self.body = body
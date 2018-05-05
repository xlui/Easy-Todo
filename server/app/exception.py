class InvalidRequest(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def json(self):
        ret = dict(self.payload or ())
        ret['status'] = self.status_code
        ret['message'] = self.message
        return ret

class CustomException(Exception):
    status = None

    def __init__(self, message, details=None, err=None, log=False):
        self.message = message
        self.details = details
        self.err = err
        self.log = log

    def form_response(self):
        if not self.message or not self.status:
            return None

        response_body = {
            "message": self.message
        }

        if self.details:
            response_body["details"] = self.details

        return response_body, self.status

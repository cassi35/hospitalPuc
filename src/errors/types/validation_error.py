class ValidationError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.status_code = 422
        self.name = 'ValidationError'
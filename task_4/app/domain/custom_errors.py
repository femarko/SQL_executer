
class ValidationError(Exception):
    """This exception is raised when a validation error occurs."""
    def __init__(self, message):
        self.message = message

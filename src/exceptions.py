class DeathException(Exception):
    def __init__(self, message):
        super().__init__(message)

class LeftTheScreenException(Exception):
    def __init__(self, message):
        super().__init__(message)
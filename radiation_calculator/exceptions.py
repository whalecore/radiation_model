class IncorrectValues(ValueError):
    def __init__(self, message):
        super(IncorrectValues, self).__init__(message)
        self.message = message
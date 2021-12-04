class ExpertaError(Exception):
    def __init__(self, message):
        super().__init__(message)


class FactNotFoundError(ExpertaError):
    """

    """

    def __init__(self):
        self.message = f"Fact wasn't found"
        super().__init__(self.message)


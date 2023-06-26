class MemRepo:
    def __init__(self, data) -> None:
        self.data = data

    def list(self):
        return self.data
from . import Representation


class BinaryRepresentation(Representation):

    def __init__(self, data) -> None:
        self.x = data

    def get(self):
        return self.x

from .Component import Component

class Tag(Component):
    def __init__(self, id: str, params: list, tagName: str, maxLenLine: int, indentation=0):
        super().__init__(id, indentation)
        self.tagName = tagName
        self.id = id
        self.params = params
        self.maxLenLine = maxLenLine

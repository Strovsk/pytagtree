class Document:
    def __init__(self, allowOverride=False, globalIndent=2, globalLineSize=150) -> None:
        self.items = {}
        self.override = allowOverride
        self.indentation = globalIndent
        self.maxLineSize = globalLineSize

    def push(self, item):
        if item.id in self.items and not self.override:
            raise RuntimeError(
                "You cannot add elements with the same Id. To aloow it, set override to True"
            )
        item.indentationSize = self.indentation
        item.maxLenLine = self.maxLineSize
        self.items[item.id] = item

    def pop(self, id):
        if id in self.items:
            del self.items[id]

    def __getContent(self):
        buffer = ""
        for tag in self.items.values():
            buffer += tag.genContent()
            buffer += "\n"
        return buffer

    def printContent(self):
        print(self.__getContent())

    def saveContentTo(self, filePath):
        with open(filePath, "w") as file:
            file.write(self.__getContent())

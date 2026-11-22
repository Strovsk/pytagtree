class Component:
    def __init__(
        self,
        ComponentName="Component",
        indentationSize=2,
        indentation=0,
        noSlashAtEnd=False,
    ):
        self.children = []
        self.__contentBase = ComponentName
        self.__content = ""
        self.__indentation = indentation
        self.indentationSize = indentationSize
        self.hasSlashAtEnd = not noSlashAtEnd
        # Value rendered inline (or already line-broken) when there are no children
        self.componentValue = ""
        # Raw text rendered on its own line before the children (mixed content)
        self.componentText = ""

    def push(self, item):
        item.addIndentation(self.__indentation)
        self.children.append(item)

    def pop(self, id: str):
        for i in range(len(self.children)):
            if self.children[i].id == id:
                self.children[i].removeIndentation(self.__indentation)
                del self.children[i]
                return 0
        return -1

    def __renderIndentation(self, size=-1):
        if size == -1:
            size = self.__indentation
        return " " * (self.indentationSize * size)

    def addIndentation(self, fatherIndentation):
        self.__indentation = fatherIndentation + 1
        for child in self.children:
            child.addIndentation(self.__indentation)

    def removeIndentation(self, fatherIndentation):
        self.__indentation = fatherIndentation - 1
        for child in self.children:
            child.removeIndentation(self.__indentation)

    def applySettings(self, indentationSize=None, maxLenLine=None):
        """Apply indentation size and max line length to this node and its subtree."""
        if indentationSize is not None:
            self.indentationSize = indentationSize
        if maxLenLine is not None and hasattr(self, "maxLenLine"):
            self.maxLenLine = maxLenLine
        for child in self.children:
            child.applySettings(indentationSize, maxLenLine)

    def _selfClosingDecorator(self):
        return "/>" if self.hasSlashAtEnd else ">"

    def genContent(self):
        indent = self.__renderIndentation()
        openTag = f"<{self.__contentBase + self.__content}"
        endTag = f"</{self.__contentBase}>"

        if len(self.children) == 0:
            if self.componentValue != "":
                return f"{indent}{openTag}>{self.componentValue}{endTag}"
            return f"{indent}{openTag}{self._selfClosingDecorator()}"

        parts = [f"{indent}{openTag}>"]
        if self.componentText != "":
            childIndent = self.__renderIndentation(self.__indentation + 1)
            parts.append(f"{childIndent}{self.componentText}")
        parts.extend(child.genContent() for child in self.children)
        parts.append(f"{indent}{endTag}")
        return "\n".join(parts)

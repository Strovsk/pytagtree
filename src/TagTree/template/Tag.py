from html import escape

from .Component import Component


class Raw(str):
    """Text that is inserted as-is, without HTML escaping.

    Use it for trusted markup only, e.g. ``Tag("div", "d", [], 80, innerText=Raw("<b>x</b>"))``.
    """


def escapeText(value) -> str:
    if isinstance(value, Raw):
        return str(value)
    return escape(str(value), quote=False)


def escapeAttribute(value) -> str:
    if isinstance(value, Raw):
        return str(value)
    return escape(str(value), quote=True)


class Tag(Component):
    def __init__(
        self,
        tagName: str,
        id: str,
        params: list,
        maxLenLine: int,
        indentation=2,
        innerText="",
        noSlashAtEnd=False,
        hideId=False,
    ):
        self.innerText = innerText
        if len(str(self.innerText)) > 0:
            noSlashProcessed = True
        else:
            noSlashProcessed = noSlashAtEnd
        super().__init__(tagName, indentation, 0, noSlashProcessed)
        self.tagName = tagName
        self.id = id
        self.hideId = hideId
        self.params = []
        self.noValueParams = []
        self.parent = self.id
        for param in params:
            if type(param) is tuple:
                self.params.append(param)
            else:
                self.noValueParams.append(param)

        if not hideId:
            self.params.insert(0, ("id", id))

        self.maxLenLine = maxLenLine
        self.lenFormattedSize = len(f"<{self.tagName}>") * 2
        self.__paramsBroken = False

    def genContent(self):
        # Rendering must not change the tag state, so the same tree always gives
        # the same output, no matter how many times it is rendered.
        self.lenFormattedSize = len(f"<{self.tagName}>") * 2
        formattedParams = self.getFormattedParams()
        self._Component__content = formattedParams
        self.componentText = escapeText(self.innerText)
        self.componentValue = self.getFormattedValue()
        return super().genContent()

    def getFormattedParams(self):
        self.__paramsBroken = False
        if len(self.params) == 0 and len(self.noValueParams) == 0:
            return ""

        formattedParams = [f'{f[0]}="{escapeAttribute(f[1])}"' for f in self.params]
        formattedParams.extend(str(p) for p in self.noValueParams)

        formattedParamsLen = len(" ".join(formattedParams)) + self.lenFormattedSize
        if formattedParamsLen >= self.maxLenLine:
            self.__paramsBroken = True
            indent = self._Component__renderIndentation(
                self._Component__indentation + 1
            )
            # format the params list to breaked param list
            formattedParams = f"\n{indent}".join(formattedParams)
            formattedParams = f"\n{indent}" + formattedParams
            formattedParams += f"\n{self._Component__renderIndentation()}"
        else:
            formattedParams = " " + " ".join(formattedParams)
        self.lenFormattedSize += len(formattedParams)
        return formattedParams

    def _selfClosingDecorator(self):
        if self.hasSlashAtEnd and not self.__paramsBroken:
            return " />"
        return super()._selfClosingDecorator()

    def getFormattedValue(self):
        text = escapeText(self.innerText)
        if text == "":
            return ""
        buffer = text
        if self.lenFormattedSize + len(text) >= self.maxLenLine or (
            self.lenFormattedSize >= self.maxLenLine
        ):
            indent = self._Component__indentation
            childIndent = self._Component__renderIndentation(indent + 1)
            buffer = f"\n{childIndent}{buffer}\n{self._Component__renderIndentation()}"
        return buffer

    def push(self, item):
        if item.id == self.id or item.id == self.parent:
            return -1
        item.parent = self.id
        super().push(item)

from .Component import Component

class Tag(Component):
    def __init__(self, tagName: str, id: str, params: list, maxLenLine: int, indentation=2, noSlashAtEnd = False, hideId = False):
        super().__init__(tagName, indentation, 0, noSlashAtEnd)
        self.tagName = tagName
        self.id = id
        self.hideId = hideId
        self.params = []
        self.noValueParams = []
        for param in params:
            if type(param) == tuple:
                self.params.append(param)
            else:
                self.noValueParams.append(param)

        if not hideId:
            self.params.insert(0, ('id', id))

        self.maxLenLine = maxLenLine
    
    def genContent(self):
        # Create the params List
        formattedParams = self.getFormattedParams()
        # Add the params list
        self._Component__content += formattedParams
        return super().genContent()
    
    def getFormattedParams(self):
        formattedParams = [
            f'{f[0]}="{f[1]}"' for f in self.params
        ]
        for noValueParam in self.noValueParams:
            formattedParams.append(noValueParam)

        formattedParamsLen = len(' '.join(formattedParams)) + len(self.tagName)
        if formattedParamsLen >= self.maxLenLine:
            indent = self._Component__renderIndentation(self._Component__indentation + 1)
            formattedParams = f'\n{indent}'.join(formattedParams)
            formattedParams = f'\n{indent}' + formattedParams
            formattedParams += f'\n{self._Component__renderIndentation()}'
        else:
            formattedParams = ' '.join(formattedParams)
            formattedParams = ' ' + formattedParams
        return formattedParams
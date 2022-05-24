from .Component import Component
import os
class Tag(Component):
    def __init__(self, tagName: str, id: str, params: list, maxLenLine: int, indentation=2, innerText = '', noSlashAtEnd = False, hideId = False):
        super().__init__(tagName, indentation, 0, noSlashAtEnd)
        self.tagName = tagName
        self.id = id
        self.hideId = hideId
        self.innerText = innerText
        self.params = []
        self.noValueParams = []
        self.parent = self.id
        for param in params:
            if type(param) == tuple:
                self.params.append(param)
            else:
                self.noValueParams.append(param)

        if not hideId:
            self.params.insert(0, ('id', id))

        self.maxLenLine = maxLenLine
        self.lenFormattedSize = (len(f'<{self.tagName}>') * 2)
    
    def genContent(self):
        # Create the params List
        formattedParams = self.getFormattedParams()
        # Add the params list
        self._Component__content = ''
        self._Component__content += formattedParams
        self.componentValue = self.getFormattedValue()
        return super().genContent()
    
    def getFormattedParams(self):
        if len(self.params) == 0 and len(self.noValueParams) == 0:
            if self.hasSlashAtEnd: return ' '
            return ''

        formattedParams = [
            f'{f[0]}="{f[1]}"' for f in self.params
        ]
        for noValueParam in self.noValueParams:
            formattedParams.append(noValueParam)

        formattedParamsLen = len(' '.join(formattedParams)) + self.lenFormattedSize
        if formattedParamsLen >= self.maxLenLine:
            indent = self._Component__renderIndentation(self._Component__indentation + 1)
            # format the params list to breaked param list
            formattedParams = f'\n{indent}'.join(formattedParams)
            formattedParams = f'\n{indent}' + formattedParams
            formattedParams += f'\n{self._Component__renderIndentation()}'
        else:
            formattedParams = ' '.join(formattedParams)
            formattedParams = ' ' + formattedParams
            if self.hasSlashAtEnd:
                formattedParams += ' '
        self.lenFormattedSize += len(formattedParams)
        return formattedParams
    
    def getFormattedValue(self):
        if self.innerText == '': return ''
        buffer = self.innerText
        if self.lenFormattedSize + len(self.innerText) >= self.maxLenLine or (
            self.lenFormattedSize >= self.maxLenLine
        ):
            indent = self._Component__indentation
            childIndent = self._Component__renderIndentation(indent + 1)
            buffer = f'\n{childIndent}{buffer}\n{self._Component__renderIndentation()}'
        return buffer
    
    def push(self, item):
        if item.id == self.id or item.id == self.parent: return -1
        item.parent = self.id
        super().push(item)

from .Component import Component

class Tag(Component):
    def __init__(self, id: str, tagName: str, params: list, maxLenLine: int, indentation=0):
        super().__init__(tagName, indentation)
        self.tagName = tagName
        self.id = id
        self.params = params
        self.params.insert(0, ('id', id))
        self.maxLenLine = maxLenLine
    
    def genContent(self):
        # Cria uma lista de parâmetros
        # formattedParams = [
        #     f'{f[0]}="{f[1]}"' for f in self.params
        # ]
        formattedParams = self.getFormattedParams()
        # Adciona a lista de parâmetros após o id
        self._Component__content += formattedParams
        return super().genContent()
    
    def getFormattedParams(self):
        formattedParams = [
            f'{f[0]}="{f[1]}"' for f in self.params
        ]
        formattedParamsLen = len(' '.join(formattedParams)) + len(self.tagName)
        if formattedParamsLen >= self.maxLenLine:
            indent = self._Component__renderIndentation(self._Component__indentation + 1)
            formattedParams = f'\n{indent}'.join(formattedParams)
            formattedParams = f'\n{indent}' + formattedParams
            formattedParams += '\n'
        else:
            formattedParams = ' '.join(formattedParams)
            formattedParams = ' ' + formattedParams
        print('result ', formattedParams)
        return formattedParams
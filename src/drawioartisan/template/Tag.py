from .Component import Component

class Tag(Component):
    def __init__(self, id: str, tagName: str, params: list, maxLenLine: int, indentation=0):
        super().__init__(id, indentation)
        self.tagName = tagName
        self.id = id
        self.params = params
        self.maxLenLine = maxLenLine
    
    def genContent(self):
        # Cria uma lista de parâmetros
        formattedParams = [
            f'{f[0]}="{f[1]}"' for f in self.params
        ]
        # Adciona a lista de parâmetros após o id
        self._Component__content += ' ' + ' '.join(formattedParams)
        return super().genContent()

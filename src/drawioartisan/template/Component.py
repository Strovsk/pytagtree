import re

class Component:
    def __init__(self, treeId, indentation = 0):
        self.children = []
        self.__contentBase = f'Component id="{str(treeId)}"'
        # self.__content = self.__contentBase
        self.__content = ''
        self.__indentation = indentation
    
    def push(self, item):
        item.addIndentation(self.__indentation)
        self.children.append(item)
    
    def __renderIndentation(self):
        return ''.join(['  ' for i in range(self.__indentation)])
    
    def addIndentation(self, fatherIndentation):
        self.__indentation = fatherIndentation + 1
        if self.children == 0: return
        for child in self.children:
            child.addIndentation(self.__indentation)
        
    def removeIndentation(self, fatherIndentation):
        self.__indentation = fatherIndentation - 1
        if self.children == 0: return
        for child in self.children:
            child.removeIndentation(self.__indentation)
    
    def genContent(self):
        if len(self.children) == 0:
            indent = self.__renderIndentation()
            return (
                re.sub(
                    r'^(.*)',
                    f'{indent}<\g<1> />',
                    self.__contentBase + self.__content,
                    0,
                    re.M
                )
            )
        buffer = ''
        for child in self.children:
            buffer += (
                '\n' +
                child.genContent()
            )
        firstTagPart = f'{self.__renderIndentation()}<{self.__contentBase + self.__content}>'
        endTag = f'\n{self.__renderIndentation()}</{self.__contentBase}>'
        return firstTagPart + buffer + endTag

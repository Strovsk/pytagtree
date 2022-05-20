import re

# TODO accept tags wich selfclose has no "/"
# TODO Accept to load content with value. Ex: "<h1 params>content</h1>"
# TODO add an hideIdFromParams. Because tags like <DOCTYPE> no need id

class Component:
    def __init__(self, ComponentName = 'Component', indentationSize = 2, indentation = 0, noSlashAtEnd = False):
        self.children = []
        self.__contentBase = ComponentName
        # self.__content = self.__contentBase
        self.__content = ''
        self.__indentation = indentation
        self.indentationSize = indentationSize
        self.hasSlashAtEnd = not noSlashAtEnd
    
    def push(self, item):
        item.addIndentation(self.__indentation)
        self.children.append(item)
    
    def __renderIndentation(self, size = -1):
        if size == -1:
            return ''.join([''.join([' ' for j in range(self.indentationSize)]) for i in range(self.__indentation)])
            # return ''.join(['  ' for i in range(self.__indentation)])
        return ''.join([''.join([' ' for j in range(self.indentationSize)]) for i in range(size)])
    
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
            if self.hasSlashAtEnd: 
                finalDecorator = '/>'
            else:
                finalDecorator = '>'
            return f'{indent}<{self.__contentBase + self.__content}{finalDecorator}'
        buffer = ''
        for child in self.children:
            buffer += (
                '\n' +
                child.genContent()
            )
        firstTagPart = f'{self.__renderIndentation()}<{self.__contentBase + self.__content}>'
        endTag = f'\n{self.__renderIndentation()}</{self.__contentBase}>'
        return firstTagPart + buffer + endTag

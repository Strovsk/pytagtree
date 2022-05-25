import sys
import os
import unittest

sys.path.append(os.path.abspath('../src'))
from TagTree.template.Tag import Tag

def getContentModel():
    path = f'./helpers/tagFileModel.model.html'
    file = open(path, 'r')
    data = [f[:-1] for f in file.readlines()]
    file.close()
    return data

def digestTestName(testName):
    replaced = testName.replace('_', ' ')
    return  replaced[0].upper() + replaced[1:]

class TagTest(unittest.TestCase):
    def test_closed_tag_have_no_slash_id_1(self):
        '''Self closed Tag have right format (only one no value param, hidden id, no slash)'''
        data = getContentModel()[0]
        tagTest = Tag(
            '!DOCTYPE',
            'doctypeId',
            ['html'],
            90,
            2,
            '',
            True,
            True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_closed_tag_have_no_slash_id_2(self):
        '''Self closed Tag have right format (slash, value params and no value params)'''
        data = getContentModel()[12][4:]
        tagTest = Tag(
            'img',
            'imgId',
            [
                ('src', '../../Assets/Logo.png'),
                ('alt', 'TagTree Logo'),
                'fakeParamA',
                'fakeParamB' 
            ],
            255,
            2,
            '',
            False,
            True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass
    
    def test_closed_tag_have_no_slash_id_3(self):
        '''Self closed Tag have right format (empty tag)'''
        data = getContentModel()[11][2:]
        tagTest = Tag(
            'body',
            'bodyId',
            [],
            255,
            2,
            '',
            True,
            True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_closed_tag_have_no_slash_id_4(self):
        '''Self closed Tag have right format (only slash)'''
        data = getContentModel()[18][4:]
        tagTest = Tag(
            'input',
            'inputId',
            [],
            255,
            2,
            '',
            False,
            True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def load_tests(self):
        buffer = []
        for method in dir(self):
            if method.find('test_') != -1:
                buffer.append(method)
        return buffer

def suite():
    s = unittest.TestSuite()
    for test in TagTest().load_tests():
        s.addTest(TagTest(test))
    return s

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

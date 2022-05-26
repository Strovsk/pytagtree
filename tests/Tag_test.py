import sys
import os
import unittest
import re

sys.path.append(os.path.abspath('../src'))
from TagTree.template.Tag import Tag

def getContentModel(testId):
    path = f'./helpers/model.txt'
    file = open(path, 'r')
    data = file.read()
    file.close()
    tagstestlist = re.findall(r'\[(.*?)\]', data, re.DOTALL | re.MULTILINE)
    return ({
        "emptyTag": tagstestlist[0],
        "emptyTagSlash": tagstestlist[1],
        "paramTag": tagstestlist[2],
        "paramTagSlash": tagstestlist[3],
        "paramValueTag": tagstestlist[4],
        "paramValueTagSlash": tagstestlist[5],
        "paramsTag": tagstestlist[6],
        "paramsTagSlash": tagstestlist[7]
    })[testId]

def digestTestName(testName):
    replaced = testName.replace('_', ' ')
    return  replaced[0].upper() + replaced[1:]

class TagTest(unittest.TestCase):
    def test_tag_has_right_format_id_1(self):
        '''Self closed Tag have right format (no id, no slash, no params)'''
        data = getContentModel('emptyTag')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[],
            maxLenLine=5,
            indentation=2,
            noSlashAtEnd=True,
            hideId=True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_2(self):
        '''Self closed Tag have right format (no id, slash, no params)'''
        data = getContentModel('emptyTagSlash')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[],
            maxLenLine=5,
            indentation=2,
            hideId=True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_3(self):
        '''Self closed Tag have right format (no id, no slash, one param)'''
        data = getContentModel('paramTag')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('param')],
            maxLenLine=25,
            indentation=2,
            hideId=True,
            noSlashAtEnd=True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_4(self):
        '''Self closed Tag have right format (no id, slash, one param)'''
        data = getContentModel('paramTag')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('param')],
            maxLenLine=25,
            indentation=2,
            hideId=True,
            noSlashAtEnd=True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_5(self):
        '''Self closed Tag have right format (no id, no slash, value param)'''
        data = getContentModel('paramValueTag')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value')],
            maxLenLine=25,
            indentation=2,
            hideId=True,
            noSlashAtEnd=True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_6(self):
        '''Self closed Tag have right format (no id, slash, value param)'''
        data = getContentModel('paramValueTagSlash')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value')],
            maxLenLine=25,
            indentation=2,
            hideId=True,
            noSlashAtEnd=False
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_7(self):
        '''Self closed Tag have right format (no id, no slash, params)'''
        data = getContentModel('paramsTag')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value'), 'param'],
            maxLenLine=60,
            indentation=2,
            hideId=True,
            noSlashAtEnd=True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_8(self):
        '''Self closed Tag have right format (no id, slash, params)'''
        data = getContentModel('paramsTagSlash')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value'), 'param'],
            maxLenLine=60,
            indentation=2,
            hideId=True,
            noSlashAtEnd=False
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

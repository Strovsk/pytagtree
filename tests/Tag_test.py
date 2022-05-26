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
        "paramsTagSlash": tagstestlist[7],
        "paramsTagId": tagstestlist[8],
        "paramsTagIdSlash": tagstestlist[9],
        "params2TagId": tagstestlist[10],
        "params2TagIdSlash": tagstestlist[11],
        "emptyTagBreak": tagstestlist[12],
        "emptyTagBreakSlash": tagstestlist[13],
        "valueParamTagBreak": tagstestlist[14],
        "valueParamTagBreakSlash": tagstestlist[15],
        "paramsTagBreak": tagstestlist[16],
        "paramsTagBreakSlash": tagstestlist[17],
        "paramsTagBreakId": tagstestlist[18],
        "paramsTagBreakIdSlash": tagstestlist[19],
        "params2TagBreakId": tagstestlist[20],
        "params2TagBreakIdSlash": tagstestlist[21]
    })[testId]

def digestTestName(testName):
    replaced = testName.replace('_', ' ')
    return  replaced[0].upper() + replaced[1:]

class TagTest(unittest.TestCase):
    def test_tag_has_right_format_id_01(self):
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

    def test_tag_has_right_format_id_02(self):
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

    def test_tag_has_right_format_id_03(self):
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

    def test_tag_has_right_format_id_04(self):
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

    def test_tag_has_right_format_id_05(self):
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

    def test_tag_has_right_format_id_06(self):
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

    def test_tag_has_right_format_id_07(self):
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

    def test_tag_has_right_format_id_08(self):
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

    def test_tag_has_right_format_id_09(self):
        '''Self closed Tag have right format (id, no slash, params)'''
        data = getContentModel('paramsTagId')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value'), 'param'],
            maxLenLine=60,
            indentation=2,
            hideId=False,
            noSlashAtEnd=True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_10(self):
        '''Self closed Tag have right format (id, slash, params)'''
        data = getContentModel('paramsTagIdSlash')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value'), 'param'],
            maxLenLine=60,
            indentation=2,
            hideId=False,
            noSlashAtEnd=False
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_11(self):
        '''Self closed Tag have right format (id, no slash, params)'''
        data = getContentModel('params2TagId')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value'), 'param', 'param2'],
            maxLenLine=60,
            indentation=2,
            hideId=False,
            noSlashAtEnd=True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_12(self):
        '''Self closed Tag have right format (id, slash, params)'''
        data = getContentModel('params2TagIdSlash')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value'), 'param', 'param2'],
            maxLenLine=60,
            indentation=2,
            hideId=False,
            noSlashAtEnd=False
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_13(self):
        '''Self closed Tag have right format (no id, no slash, no params, break)'''
        data = getContentModel('emptyTagBreak')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=['param'],
            maxLenLine=0,
            indentation=2,
            hideId=True,
            noSlashAtEnd=True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_14(self):
        '''Self closed Tag have right format (no id, slash, no params, break)'''
        data = getContentModel('emptyTagBreakSlash')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=['param'],
            maxLenLine=0,
            indentation=2,
            hideId=True,
            noSlashAtEnd=False
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_15(self):
        '''Self closed Tag have right format (no id, slash, no params, break)'''
        data = getContentModel('valueParamTagBreak')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value')],
            maxLenLine=0,
            indentation=2,
            hideId=True,
            noSlashAtEnd=True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_16(self):
        '''Self closed Tag have right format (no id, slash, no params, break)'''
        data = getContentModel('valueParamTagBreakSlash')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value')],
            maxLenLine=0,
            indentation=2,
            hideId=True,
            noSlashAtEnd=False
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_17(self):
        '''Self closed Tag have right format (no id, no slash, params, break)'''
        data = getContentModel('paramsTagBreak')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value'), 'param'],
            maxLenLine=0,
            indentation=2,
            hideId=True,
            noSlashAtEnd=True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_18(self):
        '''Self closed Tag have right format (no id, slash, params, break)'''
        data = getContentModel('paramsTagBreakSlash')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value'), 'param'],
            maxLenLine=0,
            indentation=2,
            hideId=True,
            noSlashAtEnd=False
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_19(self):
        '''Self closed Tag have right format (id, no slash, params, break)'''
        data = getContentModel('paramsTagBreakId')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value'), 'param'],
            maxLenLine=0,
            indentation=2,
            hideId=False,
            noSlashAtEnd=True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_20(self):
        '''Self closed Tag have right format (id, slash, params, break)'''
        data = getContentModel('paramsTagBreakIdSlash')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value'), 'param'],
            maxLenLine=0,
            indentation=2,
            hideId=False,
            noSlashAtEnd=False
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_21(self):
        '''Self closed Tag have right format (id, no slash, params, break)'''
        data = getContentModel('params2TagBreakId')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value'), 'param', 'param2'],
            maxLenLine=0,
            indentation=2,
            hideId=False,
            noSlashAtEnd=True
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_22(self):
        '''Self closed Tag have right format (id, slash, params, break)'''
        data = getContentModel('params2TagBreakIdSlash')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value'), 'param', 'param2'],
            maxLenLine=0,
            indentation=2,
            hideId=False,
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

from .getContentModel import getContentModel
import sys
import os
import unittest

sys.path.append(os.path.abspath('../src'))
from TagTree.template.Tag import Tag

class testsClosedInlineTags(unittest.TestCase):
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
        data = getContentModel('paramTagSlash')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('param')],
            maxLenLine=25,
            indentation=2,
            hideId=True,
            noSlashAtEnd=False
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

    def load_tests(self):
        return [test for test in dir(self) if test.find('test_') != -1]

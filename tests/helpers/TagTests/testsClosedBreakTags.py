from .getContentModel import getContentModel
import sys
import os
import unittest

sys.path.append(os.path.abspath('../src'))
from TagTree.template.Tag import Tag

class testsClosedBreakTags(unittest.TestCase):
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
        '''Self closed Tag have right format (no id, no slash, no params, break)'''
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
        return [test for test in dir(self) if test.find('test_') != -1]

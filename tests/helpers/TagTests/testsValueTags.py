from .getContentModel import getContentModel
import sys
import os
import unittest

sys.path.append(os.path.abspath('../src'))
from TagTree.template.Tag import Tag

class testsValueTags(unittest.TestCase):
    
    def test_tag_has_right_format_id_23(self):
        '''Self closed Tag have right format (no id, slash or not, params, break)'''
        data = getContentModel('emptyTagValue')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[],
            maxLenLine=160,
            indentation=2,
            hideId=True,
            noSlashAtEnd=True,
            innerText='value'
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_24(self):
        '''Self closed Tag have right format (no id, slash or not, params, break)'''
        data = getContentModel('emptyTagBreakValue')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[],
            maxLenLine=0,
            indentation=2,
            hideId=True,
            noSlashAtEnd=True,
            innerText='too long value value'
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_25(self):
        '''Self closed Tag have right format (no id, slash or not, params, break)'''
        data = getContentModel('paramTagValue')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=['param'],
            maxLenLine=160,
            indentation=2,
            hideId=True,
            noSlashAtEnd=True,
            innerText='value'
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_26(self):
        '''Self closed Tag have right format (no id, slash or not, params, break)'''
        data = getContentModel('paramTagBreakValue')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=['param'],
            maxLenLine=30,
            indentation=2,
            hideId=True,
            noSlashAtEnd=True,
            innerText='too long value value'
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_27(self):
        '''Self closed Tag have right format (no id, slash or not, params, break)'''
        data = getContentModel('paramsTagValue')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value'), 'param'],
            maxLenLine=160,
            indentation=2,
            hideId=True,
            noSlashAtEnd=True,
            innerText='Self Service'
        )
        self.assertEqual(tagTest.genContent(), data)
        pass

    def test_tag_has_right_format_id_28(self):
        '''Self closed Tag have right format (no id, slash or not, params, break)'''
        data = getContentModel('paramsTagBreakValue')
        tagTest = Tag(
            tagName='tag',
            id='tagId',
            params=[('key', 'value'), 'param'],
            maxLenLine=30,
            indentation=2,
            hideId=True,
            noSlashAtEnd=False,
            innerText='Self Service'
        )
        self.assertEqual(tagTest.genContent(), data)
        pass
    
    def load_tests(self):
        return [test for test in dir(self) if test.find('test_') != -1]

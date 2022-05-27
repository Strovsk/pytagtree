from helpers.TagTests import *
import sys
import os
import unittest

sys.path.append(os.path.abspath('../src'))
from TagTree.template.Tag import Tag

def digestTestName(testName):
    replaced = testName.replace('_', ' ')
    return  replaced[0].upper() + replaced[1:]

def suite():
    s = unittest.TestSuite()
    for test in testsClosedInlineTags().load_tests():
        s.addTest(testsClosedInlineTags(test))

    for test in testsValueTags().load_tests():
        s.addTest(testsValueTags(test))

    for test in testsClosedBreakTags().load_tests():
        s.addTest(testsClosedBreakTags(test))


    return s

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

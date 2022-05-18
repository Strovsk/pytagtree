import sys
import os
import unittest

sys.path.append(os.path.abspath('..'))
from drawioartisan.template.Tag import Tag

class TagTest(unittest.TestCase):
    def test_returnFormattedTag(self):
        # Should return the right formatted string when line is not greater than limit 80
        lineLimit = 80
        main = Tag(
            'MainTag',
            'idMainTag',
            [
                ('param1', 'value1'),
                ('param2', 'value2'),
                ('param3', 'value3')
            ],
            lineLimit,
            2
        )
        expected = '<MainTag id="idMainTag" param1="value1" param2="value2" param3="value3" />'
        self.assertEqual(main.genContent(), expected)

        # Should Break Line the line is greater than limit
        lineLimit = 50
        main = Tag(
            'MainTag',
            'idMainTag',
            [
                ('param1', 'value1'),
                ('param2', 'value2'),
                ('param3', 'value3')
            ],
            lineLimit,
            2
        )
        expected = '<MainTag\n  id="idMainTag"\n  param1="value1"\n  param2="value2"\n  param3="value3"\n/>'
        self.assertEqual(main.genContent(), expected)
    
    def test_returnRightModelWithChildrenNodes(self):
        # Should return the right formatted string when line is not greater than limit 80
        lineLimit = 80
        main = Tag(
            'MainTag',
            'idMainTag',
            [
                ('param1', 'value1'),
                ('param2', 'value2'),
                ('param3', 'value3')
            ],
            lineLimit,
            2
        )
        child = Tag(
            'ChildTag',
            'idChildTag',
            [
                ('param1', 'value1'),
                ('param2', 'value2'),
                ('param3', 'value3')
            ],
            lineLimit,
            2
        )
        main.push(child)
        expected = '<MainTag id="idMainTag" param1="value1" param2="value2" param3="value3" >\n  <ChildTag id="idChildTag" param1="value1" param2="value2" param3="value3" />\n</MainTag>'
        self.assertEqual(main.genContent(), expected)

        # Should Break Line the line is greater than limit
        lineLimit = 50
        main = Tag(
            'MainTag',
            'idMainTag',
            [
                ('param1', 'value1'),
                ('param2', 'value2'),
                ('param3', 'value3')
            ],
            lineLimit,
            2
        )
        child = Tag(
            'ChildTag',
            'idChildTag',
            [
                ('param1', 'value1'),
                ('param2', 'value2'),
                ('param3', 'value3')
            ],
            lineLimit,
            2
        )
        main.push(child)
        expected = '<MainTag\n  id="idMainTag"\n  param1="value1"\n  param2="value2"\n  param3="value3"\n>\n  <ChildTag\n    id="idChildTag"\n    param1="value1"\n    param2="value2"\n    param3="value3"\n  />\n</MainTag>'

        self.assertEqual(main.genContent(), expected)

if __name__ == '__main__':
    unittest.main()

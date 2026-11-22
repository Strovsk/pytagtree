import os
import sys
import tempfile
import unittest

sys.path.append(os.path.abspath("../src"))
from TagTree import Document, Raw, Tag


def tag(name, id, params=None, maxLen=150, **kwargs):
    return Tag(name, id, params or [], maxLen, **kwargs)


class EscapingTest(unittest.TestCase):
    def test_text_is_escaped(self):
        p = tag("p", "p", hideId=True, innerText="<script>alert(1)</script> & x")
        self.assertEqual(
            p.genContent(), "<p>&lt;script&gt;alert(1)&lt;/script&gt; &amp; x</p>"
        )

    def test_attribute_value_is_escaped(self):
        a = tag("a", "a", [("title", "a\"b<c>&'")], hideId=True)
        self.assertEqual(a.genContent(), '<a title="a&quot;b&lt;c&gt;&amp;&#x27;" />')

    def test_id_is_escaped(self):
        self.assertEqual(tag("i", 'x"y').genContent(), '<i id="x&quot;y" />')

    def test_raw_skips_escaping(self):
        div = tag("div", "d", hideId=True, innerText=Raw("<b>bold</b>"))
        self.assertEqual(div.genContent(), "<div><b>bold</b></div>")

    def test_non_string_values(self):
        el = tag("data", "d", [("value", 3)], hideId=True, innerText=5)
        self.assertEqual(el.genContent(), '<data value="3">5</data>')


class IdempotencyTest(unittest.TestCase):
    def test_same_output_on_every_call(self):
        el = tag("p", "x", [("a", "b")], maxLen=40, innerText="y" * 12)
        first = el.genContent()
        self.assertEqual(first, '<p id="x" a="b">yyyyyyyyyyyy</p>')
        self.assertEqual(el.genContent(), first)
        self.assertEqual(el.genContent(), first)

    def test_tree_output_is_stable(self):
        root = tag("ul", "u", [("class", "list")], maxLen=20)
        root.push(tag("li", "l", innerText="item"))
        self.assertEqual(root.genContent(), root.genContent())


class OpeningTagTest(unittest.TestCase):
    def test_no_trailing_space_with_children(self):
        a = tag("a", "x")
        a.push(tag("span", "s", innerText="hi"))
        self.assertEqual(a.genContent(), '<a id="x">\n  <span id="s">hi</span>\n</a>')

    def test_no_trailing_space_without_params(self):
        div = tag("div", "d", hideId=True)
        div.push(tag("br", "b", hideId=True))
        self.assertEqual(div.genContent(), "<div>\n  <br />\n</div>")

    def test_self_closing_keeps_space_before_slash(self):
        self.assertEqual(
            tag("input", "i", ["disabled"]).genContent(), '<input id="i" disabled />'
        )


class MixedContentTest(unittest.TestCase):
    def test_text_is_kept_alongside_children(self):
        p = tag("p", "p", hideId=True, innerText="Hello")
        p.push(tag("b", "b", hideId=True, innerText="world"))
        self.assertEqual(p.genContent(), "<p>\n  Hello\n  <b>world</b>\n</p>")

    def test_text_alongside_children_is_escaped(self):
        p = tag("p", "p", hideId=True, innerText="1 < 2")
        p.push(tag("br", "b", hideId=True))
        self.assertEqual(p.genContent(), "<p>\n  1 &lt; 2\n  <br />\n</p>")


class DocumentTest(unittest.TestCase):
    def build(self):
        html = tag("html", "h", hideId=True)
        body = tag("body", "b", hideId=True)
        html.push(body)
        body.push(tag("p", "p", hideId=True, innerText="ção"))
        return html

    def test_global_indent_reaches_every_level(self):
        doc = Document(globalIndent=4)
        doc.push(self.build())
        expected = "<html>\n    <body>\n        <p>ção</p>\n    </body>\n</html>\n"
        self.assertEqual(doc._Document__getContent(), expected)

    def test_global_indent_applies_to_children_pushed_later(self):
        doc = Document(globalIndent=3)
        html = tag("html", "h", hideId=True)
        doc.push(html)
        html.push(tag("body", "b", hideId=True))
        self.assertEqual(doc._Document__getContent(), "<html>\n   <body />\n</html>\n")

    def test_save_content_writes_utf8(self):
        doc = Document()
        doc.push(self.build())
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "out.html")
            doc.saveContentTo(path)
            with open(path, "rb") as file:
                self.assertIn("ção".encode(), file.read())

    def test_save_content_error_is_chained(self):
        doc = Document()
        with self.assertRaises(RuntimeError) as ctx:
            doc.saveContentTo(os.path.join("missing-dir", "x", "out.html"))
        self.assertIsInstance(ctx.exception.__cause__, OSError)


if __name__ == "__main__":
    unittest.main()

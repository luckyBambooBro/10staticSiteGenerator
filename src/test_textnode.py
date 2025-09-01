import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_text(self):
        node = TextNode("This is the regular text", TextType.ITALIC)
        node2 = TextNode("This is different text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_different_url(self):
        node = TextNode("This is a text node", TextType.TEXT, url="google.com")
        node2 = TextNode("This is a text node", TextType.TEXT, url="youtube.com")
        self.assertNotEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()

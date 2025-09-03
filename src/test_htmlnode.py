import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode("p")
        self.assertEqual(node.tag, "p")

    def test_values(self):
        node = HTMLNode("h1", "lorem ipsum", None, {"href": "https://google.com"})
        self.assertEqual(node.tag, "h1" )
        self.assertEqual(node.value, "lorem ipsum")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"href": "https://google.com"})

    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"href": "https://youtube.com"})
        self.assertEqual(node.props_to_html(), " href=\"https://youtube.com\"")

    def test_repr(self):
        node = HTMLNode("p", "What a strange world", None, {"class": "primary"})
        self.assertEqual(node.__repr__(), "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})")

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://google.com\">Click me!</a>")

    def test_leaf_values(self):
        node = LeafNode("h1", "lorem ipsum")
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "lorem ipsum")


    if __name__ == "__main__":
        unittest.main()
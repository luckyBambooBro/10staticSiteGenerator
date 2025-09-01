import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode("p")
        node2 = HTMLNode("p")
        self.assertEqual(node, node2)

    def test_values(self):
        node = HTMLNode("h1", "lorem ipsum", [HTMLNode("p", None, None, None)], {"href": "https://google.com"})
        self.assertEqual(node.tag, "h1" )
        self.assertEqual(node.value, "lorem ipsum")
        self.assertEqual(node.children, [HTMLNode("p", None, None, None)])
        self.assertEqual(node.props, {"href": "https://google.com"})

    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"href": "https://youtube.com"})
        self.assertEqual(node.props_to_html(), " href=\"https://youtube.com\"")

    if __name__ == "__main__":
        unittest.main()
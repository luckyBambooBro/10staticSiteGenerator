import unittest
from htmlnode import HTMLNode

class htmlTest(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode("<p>")
        node2 = HTMLNode("<p>")
        self.assertEqual(node, node2)

    def test_value(self):
        node = HTMLNode("<h1>", "lorem ipsum")
        node2 = HTMLNode("<h1>", "lorem ipsum")
        self.assertEqual(node, node2)

    def test_different_value(self):
        node = HTMLNode("<h1>", "lorem ipsum")
        node2 = HTMLNode("<h1>", "lorem ipsum lorem ipsum")
        self.assertNotEqual(node, node2)

    def test_same_children(self):
        node = HTMLNode("<body>", "lorem ipsum", ["<h1>", "<h2>"])
        node2 = HTMLNode("<body>", "lorem ipsum", ["<h1>", "<h2>"])
        self.assertEqual(node, node2)

    def test_different_children(self):
        node = HTMLNode("<body>", "lorem ipsum", ["<h1>", "<h2>"])
        node2 = HTMLNode("<body>", "lorem ipsum", ["<h3>", "<h4>"])
        self.assertNotEqual(node, node2)

    def test_same_props(self):
        node = HTMLNode("<a>", None, None, {"href": "https://google.com"})
        node2 = HTMLNode("<a>", None, None, {"href": "https://google.com"})
        self.assertEqual(node, node2)

    def test_different_props(self):
        node = HTMLNode("<a>", None, None, {"href": "https://google.com"})
        node2 = HTMLNode("<a>", None, None, {"href": "https://youtube.com"})
        self.assertNotEqual(node, node2)
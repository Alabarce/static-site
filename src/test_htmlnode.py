import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"},)
        self.assertEqual(node.props_to_html(), ' class="greeting" href="https://boot.dev"',)

    def test_values(self):
        node = HTMLNode("div", "I wish I could read",)
        self.assertEqual(node.tag, "div",)
        self.assertEqual(node.value, "I wish I could read",)
        self.assertEqual(node.children, None,)
        self.assertEqual(node.props, None,)

    def test_repr(self):
        node = HTMLNode("p", "What a strange world",None, {"class": "primary"},)
        self.assertEqual(node.__repr__(), "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",)

    def test_leafnode_to_html(self):
        leaf = LeafNode(tag="p", value="This is a paragraph", props={"class": "text"})
        self.assertEqual(leaf.to_html(), '<p class="text">This is a paragraph</p>')

    def test_leafnode_no_tag(self):
        leaf = LeafNode(tag=None, value="Just raw text")
        self.assertEqual(leaf.to_html(), "Just raw text")
    
    def test_leafnode_children(self):
        with self.assertRaises(TypeError):
            LeafNode(tag="span", value="Leaf node", children=[HTMLNode(tag="div", value="Child node")])

    def test_leafnode_empty_value(self):
        leaf = LeafNode(tag="div", value="")
        self.assertEqual(leaf.to_html(), '<div></div>')

    def test_parentnode_children(self):
        with self.assertRaises(TypeError):
            ParentNode(tag="div", value="Parent node", children = [])

    def test_headings(self):
        node = ParentNode("h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],)
        self.assertEqual(node.to_html(), "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",)

    def test_to_html_many_children(self):
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",)



if __name__ == "__main__":
    unittest.main()
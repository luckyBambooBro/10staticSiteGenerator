from textnode import TextNode, TextType #does this need * before textnode?

def main():
    dummy = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(dummy)
main()
from textnode import TextNode, TextType


def main():
    text_node = TextNode("Hello World", TextType.PLAIN)
    print(text_node)


if __name__ == "__main__":
    main()

class UserInput(object):

    @staticmethod
    def entry_choice():
        # source = input("Please choose source plain text/file: ")
        # source = "file"
        # if source == "text":
        #     plain_text = input("Enter the text to compress: ")
        #     source = "examples/test_text.txt"
        # elif source == "file":
        # source = input("Enter the name/path to deal with: ")

        # plain_text = input("Enter the text to compress: ")
        #     source = "examples/test_text.txt"

        # source = "examples/sample.txt"
        source = "examples/sample.Dar"

        action = input("Please check compress/decompress: ")
        # compression = input("Please choose compression/decompression method (LZW/Huffman): ")

        compression = "lzw"  # fixed just for test

        if compression == "huff" or compression == "Huffman":
            compression = "huff"
        elif compression == "lzw" or compression == "LZW":
            compression = "lzw"
        if action == "c":
            action = "compress"
        elif action == "d":
            action = "decompress"

        return (compression, action, source)

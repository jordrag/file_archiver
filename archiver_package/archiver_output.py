import pickle
from struct import *


class FileOperator(object):
    def __init__(self, data_package, compression_key, action_key):
        self.data_package = data_package
        self.action_key = action_key
        self.compression_key = compression_key

    def commands(self):
        if self.compression_key == "huff" and self.action_key == "compress":
            HuffmanFiles(self.data_package).huffman_compress()
        elif self.compression_key == "huff" and self.action_key == "decompress":
            HuffmanFiles(self.data_package).huffman_decompress()

        if self.compression_key == "lzw" and self.action_key == "compress":
            LzwFiles(self.data_package).lzw_compress()
        elif self.compression_key == "lzw" and self.action_key == "decompress":
            LzwFiles(self.data_package).lzw_decompress()


class HuffmanFiles(object):
    def __init__(self, data_package):
        self.data_package = data_package
        self.huff_data = self.data_package[0]
        self.output_path = self.huff_data.output_path

    def huffman_compress(self):
        bytes_list = self.data_package[1]
        reverse_mapping = self.data_package[2]
        original_names = self.data_package[3]
        tree_path = self.huff_data.tree_path
        original_names_path = self.huff_data.original_names_path

        with open(self.output_path, 'wb') as output_file, open(tree_path, 'wb') as output_tree, \
                open(original_names_path, 'wb') as originals:
            output_file.write(bytes_list)
            pickle.dump(reverse_mapping, output_tree)
            pickle.dump(original_names, originals)

        return print("\nHuffman compressed !")

    def huffman_decompress(self):
        decompressed_text = self.data_package[1]

        with open(self.output_path, 'w', encoding='utf8') as output:
            output.write(decompressed_text)

        return print("\nHuffman decompressed !")


class LzwFiles(object):
    def __init__(self, data_package):
        self.data_package = data_package
        self.lzw_data = data_package
        self.output_file = self.lzw_data.output_file
        self.original_names_file = self.lzw_data.original_names_path
        self.original_names = self.lzw_data.original_names
        self.compressed_data = self.lzw_data.compressed_data
        self.decompressed_data = self.lzw_data.decompressed_data
        self.output_path = self.lzw_data.output_path

    def lzw_compress(self):
        with open(self.output_file, "wb") as output, open(self.original_names_file, "wb") as originals:
            pickle.dump(self.original_names, originals)
            for data in self.compressed_data:
                output.write(pack('>H', int(data)))

        return print("\nLZW compressed !")

    def lzw_decompress(self):
        with open(self.output_path, "w") as output_file:
            for data in self.decompressed_data:
                output_file.write(data)

        return print("\nLZW decompressed !")


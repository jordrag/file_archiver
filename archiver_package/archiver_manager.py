import os

from archiver_package.huffman import *
from archiver_package.lzw import *


class ArchiveManager(object):
    def __init__(self, compression, action, source):
        self.compression_key = compression
        self.action_key = action
        self.path = source
        self.source_data = self.manage_source()
        self.original_names = self.source_data[0]
        self.output_path = self.source_data[1]
        self.tree_path = self.source_data[2]
        self.original_names_path = self.source_data[3]
        self.filename = self.source_data[4]
        self.file_path = self.source_data[5]
        self.filepath_name = self.source_data[6]

    def manage_source(self):
        original_names = {}

        filepath_name, file_extension = os.path.splitext(self.path)
        original_names[filepath_name] = file_extension

        output_path = filepath_name + ".Dar"
        tree_path = filepath_name + ".tree"
        file_split = filepath_name.split("/")
        file_path = "/".join(file_split[0:len(file_split)-1])
        filename = file_split[len(file_split)-1]
        original_names_path = file_path + "/" + "original_names.pkl"

        return (original_names, output_path, tree_path, original_names_path, filename, file_path,
                filepath_name)

    def manage_compression(self):
        work_object = None
        if self.compression_key == "huff":
            work_object = HuffmanCoding(self)

        elif self.compression_key == "lzw":
            work_object = CodingLZW(self)

        if self.action_key == "compress":
            work_object = work_object.compress()

        elif self.action_key == "decompress":
            work_object = work_object.decompress()

        return work_object

# ******************************************************************************

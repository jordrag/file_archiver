from struct import *
import pickle


class CodingLZW(object):
    """
    The LZW algorithm for coding and decoding common file defined by user.
    """

    def __init__(self, input_data):
        self.filepath_name = input_data.filepath_name
        self.file_path = input_data.file_path
        self.filename = input_data.filename
        self.path = input_data.path
        self.original_names = input_data.original_names
        self.output_path = input_data.output_path
        self.original_names_path = input_data.original_names_path

        self.compressed_data = []
        self.decompressed_data = ""
        self.file = open(self.path, "rb")
        self.n = 255 # number of bits
        self.output_file = self.filepath_name + ".Dar"

    def compress(self):
        """ Makes the necessary data package for file compression. """

        maximum_table_size = pow(2, int(self.n))
        file = open(self.path)
        data = file.read()

        # Building and initializing the dictionary.
        dictionary_size = 256
        dictionary = {chr(i): i for i in range(dictionary_size)}
        string = ""  # String is null.

        # iterating through the input symbols.
        # LZW Compression algorithm
        for symbol in data:
            string_plus_symbol = string + symbol  # get input symbol.
            if string_plus_symbol in dictionary:
                string = string_plus_symbol
            else:
                self.compressed_data.append(dictionary[string])
                if (len(dictionary) <= maximum_table_size):
                    dictionary[string_plus_symbol] = dictionary_size
                    dictionary_size += 1
                string = symbol

        if string in dictionary:
            self.compressed_data.append(dictionary[string])

        return (self)

    def decompress(self):
        """ Makes the necessary data package for file decompression. """

        with open(self.original_names_path, 'rb') as originals:
            original_names = pickle.load(originals)
        self.output_path = self.filepath_name + "_decompressed_LZW" + original_names[self.filepath_name]
        maximum_table_size = pow(2, int(self.n))
        next_code = 256
        string = ""

        # Reading the compressed file.
        while True:
            rec = self.file.read(2)
            if len(rec) != 2:
                break
            (data,) = unpack('>H', rec)
            self.compressed_data.append(data)

        # Building and initializing the dictionary.
        dictionary_size = 256
        dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

        # Iterating through the compressed data by LZW decompression algorithm

        for code in self.compressed_data:
            if not (code in dictionary):
                dictionary[code] = string + (string[0])
            self.decompressed_data += dictionary[code]
            if not (len(string) == 0):
                dictionary[next_code] = string + (dictionary[code][0])
                next_code += 1
            string = dictionary[code]

        return (self)
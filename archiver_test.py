import heapq
import json
import os
from binarytree import *
import pickle
from collections import deque
from dahuffman import HuffmanCodec

string = 'In Python, everything is an object and string is an object too. ' \
        'Python string can be created simply by enclosing characters in the double quote. ' \
        'Python does not support a character type. These are treated as strings of length one, ' \
        'also considered as a substring'

# with open("sample.txt", "rb") as open_file:
#     string = open_file.read()

# print(string)
code_string = bytearray()

# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq
# print(nodes)

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    # print(nodes)
huffmanCode = huffman_code_tree(nodes[0][0])

# print(huffmanCode)
# print(' Char | Huffman code ')
# print('----------------------')
# for (char, frequency) in freq:
#     print(' %-4r |%12s' % (char, huffmanCode[char]))

for ch in string:
    code_ch = huffmanCode[ch]
    code_string.append(int(code_ch, 2))

print(code_string)
print(huffmanCode)

def decode(code_in, decode_keys):
    output_word = []
    code_in_queue = deque(code_in)
    while True:
        if len(code_in_queue) == 0:
            return output_word
        letter_code = code_in_queue.popleft()
        for new_k in decode_keys.items():
            if new_k[1] == letter_code:
                letter = new_k[0]
                output_word.append(letter)
    return output_word


output_list = decode(code_string, huffmanCode)
output_data = "".join(output_list)

print(output_list)
print(output_data)

#
# with open("sample_test.txt", "wb") as output_save:
#     output_save.write(str(code_string))
#     output_save.write(str(huffmanCode))


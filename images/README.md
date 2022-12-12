## <center> **** User manual **** </center>


*A simple file compressor(archiver) using two popular lossless methods: LZW and Huffman coding. \
In short for these methods:* 

### *A little bit theory.....*

1. **Huffman Coding** is a technique of compressing data to reduce its size without losing any of the
details. It was first developed by David Huffman. Huffman Coding is generally useful to compress the
data in which there are frequently occurring characters. First all the string is observed and a tree
is made based on the frequency of each character in it. For decoding the code, we can take the code 
and traverse through the tree to find the character. 
   * Huffman coding is used in conventional compression formats like GZIP, BZIP2, PKZIP, etc. 
   * For text and fax transmissions.

2. **Lempel–Ziv–Welch (LZW) Algorithm**  is a very common compression technique. 
It is lossless, meaning no data is lost when compressing. The algorithm is simple to implement and 
has the potential for very high throughput in hardware implementations. The Idea relies on 
reoccurring patterns to save data space. LZW is the foremost technique for general-purpose data 
compression due to its simplicity and versatility. It is the basis of many PC utilities that claim 
to “double the capacity of your hard drive”. 
   * *LZW compression works* by reading a sequence of symbols,
grouping the symbols into strings, and converting the strings into codes. Because the codes take up
less space than the strings they replace, we get compression. Characteristic features of LZW 
includes, LZW compression uses a code table, with 4096 as a common choice for the number of table 
entries. Codes 0-255 in the code table are always assigned to represent single bytes from the input 
file. When encoding begins the code table contains only the first 256 entries, with the remainder of
the table being blanks. Compression is achieved by using codes 256 through 4095 to represent 
sequences of bytes. As the encoding continues, LZW identifies repeated sequences in the data and 
adds them to the code table. Decoding is achieved by taking each code from the compressed file and 
translating it through the code table to find what character or characters it represents.
    * *Implementation* - The idea of the compression algorithm is the following: as the input data is 
being processed, a dictionary keeps a correspondence between the longest encountered words and a 
list of code values. The words are replaced by their corresponding codes and so the input file is 
compressed. Therefore, the efficiency of the algorithm increases as the number of long, repetitive 
words in the input data increases.
    * This algorithm compresses repetitive sequences of data very well. Since the codewords are 
12 bits, any single encoded character will expand the data size rather than reduce it.
    * *This algorithm is typically used* in GIF and optionally in PDF and TIFF. Unix’s ‘compress’ 
command, among other uses.  It is the algorithm of the widely used Unix file compression utility 
compress and is used in the GIF image format.

3. **Advantages of LZW over Huffman:**
    1. LZW requires no prior information about the input data stream.
    2. LZW can compress the input stream in one single pass.
    3. Another advantage of LZW is its simplicity, allowing fast execution.

### *The application*

It is managed by the command prompt and can operate with files or folders choosing one of the 
mentioned above methods. 


References:

https://www.programiz.com/dsa/heap-sort \
https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique
https://github.com/bhrigu123/huffman-coding

#
#Kelsey Deuth
#kdeuth@calpoly.edu
#06/14/19
#
#Project 3
#Section 11
#Creates a huffman tree and compresses to a file
#



class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __lt__(self, node):
        return comes_before(self, node)

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq < b.freq:
        return True
    elif b.freq > a.freq:
        return False
    elif a.char > b.char:
        return False
    else:
        return True


def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values
    take the minimum ASCII character regarless of the freq"""
    new = HuffmanNode(min(a.char, b.char), a.freq + b.freq)
    if comes_before(a, b) is True:
        new.left = a
        new.right = b
    else:
        new.left = b
        new.right = a
    return new


def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    list_of_freqs = [0] * 256
    fp = open(filename, 'r')
    for line in fp:
        for char in line:
            num = ord(char)
            list_of_freqs[num] += 1
    fp.close()
    return list_of_freqs


def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    lst = []
    counter = 0
    for freq in char_freq:
        if freq != 0:
            new = HuffmanNode(counter, freq)
            lst.append(new)
        counter += 1
    lst.sort()
    while len(lst) != 1:  #when it is the last one, that's the root!
        left = lst.pop(0)
        right = lst.pop(0)
        new = combine(left, right)
        lst.append(new)
        lst.sort()
    return lst[0]


def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    str = "" * 256
    if node is not None:
        if node.left is None and node.right:
            node.char = str[char]



def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    s = ''
    counter = 0
    for freq in freqs:
        if freq != 0:
            s = s + str(counter) + " " + str(freq) + " "
        counter += 1
    s = s.strip()
    return s


def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    header = create_header(freqs)










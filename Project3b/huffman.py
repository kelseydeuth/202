class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __lt__(self, other):
        if self.freq < other.freq:
            return True
        elif self.freq > other.freq:
            return False
        return self.char < other.char
        #return comes_before(self, other)

    def __cmp__(self, other):
        return comes_before(self, other)

    def __repr__(self):
        return str(self.char) + " " + str(self.freq) + " " + str(self.left) + str(self.right)

    # def set_left(self, node):
    #     self.left = node
    #
    # def set_right(self, node):
    #     self.right = node


def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq < b.freq:
        return True
    elif b.freq > a.freq:
        return False
    elif a.char > b.char:
        return False
    elif a.char < b.char:
        return True


def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values
    take the minimum ASCII character regarless of the freq"""
    new = HuffmanNode(min(a.char, b.char), a.freq + b.freq)
    if comes_before(a, b):
        new.left = a
        new.right = b
    else:
        new.left = b
        new.right = a
    return new


def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    freqs = [0] * 256
    fp = open(filename, 'r')
    for line in fp:
        for char in line:
            num = ord(char)
            freqs[num] += 1
    fp.close()
    return freqs


def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    lst = []
    counter = 0
    for freq in char_freq:
        if freq > 0:
            new = HuffmanNode(counter, freq)
            lst.append(new)
        counter += 1
    #lst.sort()

    while len(lst) != 1:  #when it is the last one, that's the root!
        lst.sort()

        #print([(k.char, k.freq) for k in lst])
        #left = lst.pop(0)
        #right = lst.pop(0)
        left = lst[0]
        right = lst[1]
        lst = lst[2:]

        new = combine(left, right)
        lst.append(new)
        #print(new)
        #print([(k.char, k.freq) for k in lst])
        #lst.sort()
    return lst[0]


def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the array, with the resulting Huffman code for that character stored at that location"""
    s = [""] * 256
    create_code_help(node, s, "")
    return s


def create_code_help(node, s, code):
    if node.left == None and node.right == None:
        s[node.char] = code
    if node.left != None:
        create_code_help(node.left, s, code + "0")
    if node.right != None:
        create_code_help(node.right, s, code + "1")


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
    freqs = cnt_freq(in_file)
    inf = open(in_file, "r")
    header = create_header(freqs)
    node = create_huff_tree(freqs)
    codes = create_code(node)
    body = ""
    #print(codes[97:])
    for line in inf:
        for char in line:
            # print(codes[ord(char)])
            body += codes[ord(char)]
    of = open(out_file, "w", newline="")
    of.write(header + "\n")
    of.write(body)
    inf.close()
    of.close()


def huffman_decode(encoded_file, decode_file):
    inf = open(encoded_file, "r")
    rest = inf.readlines()
    header = rest[0]
    rest.pop(0)
    freqs = parse_header(header)
    tree = create_huff_tree(freqs)
    of = open(decode_file, "w", newline="")
    a = create_code_h(tree)
    of.write(a)
    inf.close()
    of.close()

    
def create_code_h(tree):
    s = ""
    if tree.left == None and tree.right == None:
        s[node.char] = code
    if tree.left != None:
        create_code_h(tree.left, s, code + "0")
    if tree.right != None:
        create_code_h(tree.right, s, code + "1")
    return s


def parse_header(header_string):
    s = [0] * 256
    counter = 0
    header_string = header_string.split(" ")
    for num in header_string:
        if counter == 0:
            s[int(num)] = int(header_string[counter + 1])
            counter += 1
        elif counter % 2 == 0:
            s[int(num)] = int(header_string[counter + 1])
            counter += 1
        else:
            counter += 1
    return s


















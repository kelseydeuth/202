from hash_quad import *
import string


class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        # get rid of new line character
        # for line in lines
        self.stop_table = HashTable(191)
        try:
            fp = open(filename, 'r')
        except FileNotFoundError:
            raise FileNotFoundError
        for key in fp:
            key = key.rstrip()
            self.stop_table.insert(key, 0)
        fp.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.concordance_table = HashTable(191)
        try:
            fp = open(filename, 'r')
        except FileNotFoundError:
            raise FileNotFoundError
        counter = 1
        for line in fp:
            for key in line.split():
                key = key.replace("\n", '')
                key = key.replace('-', " ")
                key = key.replace(',', "")
                key = key.replace("'", '')
                key = key.replace('.', '')
                key = key.replace("''", "")
                key = key.replace("", "")
                key = key.lower()
                # if " " in key:
                #     key = ' '.split(key)
                print(key)
                if key not in self.stop_table.hash_table:
                    self.concordance_table.insert(key, counter)
            counter += 1
        fp.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        s = ''
        fp = open(filename, 'w')
        for n in self.concordance_table.hash_table:
            if n is not None:
                if n[0] not in self.stop_table.hash_table:
                    n = str(n)
                    n = n.split()
                    fp.write(n[0] + ":" + n[1] + "\n")
        fp.close()



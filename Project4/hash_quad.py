class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None] * table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted, and the value is used as the first 
        line number in the list of line numbers. If the key is in the table, then the value is appended to that 
        key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        index = self.horner_hash(key)
        # original = index
        # for i in range(self.table_size()):
        # if self.hash_table[(index + i * i) % self.table_size] is None:
        #     self.hash_table[(index + (i * i)) % self.table_size] = (index, value)
        # self.table_size += 1
        h = self.horner_hash(key)
        for i in range(self.table_size):
            if self.hash_table[(h + i * i) % self.table_size] is None:
                self.hash_table[(h + i * i) % self.table_size] = [key, [value]]
                self.num_items += 1
                break
            elif self.hash_table[(h + i * i) % self.table_size][0] is key:
                if value not in self.hash_table[(h + i * i) % self.table_size][1]:
                    self.hash_table[(h + i * i) % self.table_size][1].append(value)
                    return

        if self.get_load_factor() > .5:
            self.size_up()

    def size_up(self):
        l = [x for x in self.hash_table if x is not None]
        self.num_items = 0
        self.table_size = 2 * self.table_size + 1
        self.hash_table = [None] * self.table_size
        for value in l:
            for x in value[1]:
                self.insert(value[0], x)

    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        ans = 0
        n = min(len(key), 8)
        for i in range(n):
            math = (31 ** (n - 1 - i))
            k = ord(key[i])
            solution = k * math
            ans += solution
        return ans % self.table_size

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        h = self.horner_hash(key)
        for i in range(self.table_size):
            if self.hash_table[(h + i * i) % self.table_size]:
                if self.hash_table[h + i * i][0] is key:
                    return True
        return False

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        h = self.horner_hash(key)
        for i in range(self.table_size):
            if self.hash_table[(h + i * i) % self.table_size]:
                if self.hash_table[h + i * i][0] is key:
                    return h
        return None

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        s = []
        for n in self.hash_table:
            if n is not None:
                s.append(n[0])
        return s

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""

        if self.get_index(key):
            return self.hash_table[self.get_index(key)][1]
        return None

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size




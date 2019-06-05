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
        if self.hash_table[index] is None:
            self.hash_table[index] = (key, [value])
        elif self.hash_table[index] == index:
            self.hash_table[index][1].append(value)
        else:
            i = 1
            while self.hash_table[index] is not None and self.hash_table[index][0] != key:
                new_index = (index + (i ** 2)) % self.table_size
                i += 1
                if self.hash_table[new_index][0] is None:
                    self.hash_table[new_index][0] = key
                    self.hash_table[new_index][1] = [value]
                    self.num_items += 1
                if self.hash_table[new_index][0] == key:
                    self.hash_table[index][1].append(value)
                if new_index > len(self.hash_table):
                    index = new_index - len(self.hash_table)
        lf = self.get_load_factor()
        if lf > 0.5:
            self.size_up()

    def size_up(self):
            new_table_size = 2 * self.table_size + 1
            new_table = [None] * new_table_size
            for key, value in self.hash_table:
                new_table.self.insert(key, value)
            self.table_size = new_table_size

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
        i = self.hash_table(key)
        for n in range(0, self.table_size):
            if i == n:
                return True
        return False

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        i = self.hash_table(key)
        if self.in_table(i) is False:
            return None
        for n in range(0, self.table_size):
            if i == n:
                self.get_index(n)
                return n

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        s = []
        counter = 0
        for n in self.hash_table:
            if n is None:
                break
            elif n[counter] is not None:
                s.append(n[counter])
                counter += 1
        return s

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        n = self.get_index(key)
        if n is None:
            return None
        else:
            ans = self.hash_table[n][1]  # gets VALUE
        return ans

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size




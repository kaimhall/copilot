# hashtable.py


class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [None] * capacity

    def hash(self, key):
        return key % self.capacity

    def add(self, key, value):
        hash_key = self.hash(key)
        self.table[hash_key] = value

    def get(self, key):
        hash_key = self.hash(key)
        return self.table[hash_key]

    def remove(self, key):
        hash_key = self.hash(key)
        self.table[hash_key] = None

    def __str__(self):
        return str(self.table)

# test_hash_table.py
from hashtable import HashTable
import pytest


def test_should_create_hash_table():
    hash_table = HashTable()
    assert hash_table is not None


def test_should_create_hash_table_with_capasity():
    hash_table = HashTable(10)
    assert hash_table is not None

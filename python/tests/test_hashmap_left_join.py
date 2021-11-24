import pytest
from data_structure.hash_table.hashtable import HashTable
from code_challenges.hashmap_left_join.hashmap_left_join import left_join


def test_left_join_one():
    hashmap_one = HashTable()
    hashmap_one.add('fond', 'enamored')
    hashmap_one.add('wrath', 'anger')
    hashmap_one.add('diligent', 'employed')
    hashmap_one.add('outfit', 'garb')

    hashmap_two = HashTable()
    hashmap_two.add('fon', 'averse')
    hashmap_two.add('wra', 'delight')
    hashmap_two.add('dilit', 'idle')
    hashmap_two.add('gui', 'follow')

    actual = left_join(hashmap_one, hashmap_two)
    expected = [['fond', 'enamored', None], ['wrath', 'anger', None], ['diligent', 'employed', None], ['outfit', 'garb', None]]
    assert actual == expected

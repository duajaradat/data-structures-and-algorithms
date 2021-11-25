import pytest
from data_structure.hash_table.hashtable import HashTable
from code_challenges.hashmap_left_join.hashmap_left_join import left_join


def test_left_join_none():
    hashmap_one = HashTable()
    hashmap_one.add('foo', 'ff')
    hashmap_one.add('moo', 'mm')
    hashmap_one.add('soo', 'ss')


    hashmap_two = HashTable()
    hashmap_two.add('fo', 'f')
    hashmap_two.add('mo', 'm')
    hashmap_two.add('so', 's')


    actual = left_join(hashmap_one, hashmap_two)
    expected = [['foo', 'ff', None], ['moo', 'mm', None], ['soo', 'ss', None]]
    assert actual == expected

def test_left_join_one():
    hashmap_one = HashTable()
    hashmap_one.add('foo', 'ff')
    hashmap_one.add('moo', 'mm')
    hashmap_one.add('soo', 'ss')


    hashmap_two = HashTable()
    hashmap_two.add('foo', 'f')
    hashmap_two.add('moo', 'm')
    hashmap_two.add('soo', 's')

    actual = left_join(hashmap_one, hashmap_two)
    expected = [['foo', 'ff', 'f'], ['moo', 'mm', 'm'], ['soo', 'ss', 's']]

    assert actual == expected


def test_left_join_empty_hash():
    hashmap_one = HashTable()

    hashmap_two = HashTable()
    actual = left_join(hashmap_one, hashmap_two)
    expected = []
    assert actual == expected

# Write tests to prove the following functionality:

# - [x] Adding a key/value to your hashtable results in the   value being in the data structure
# - [x]Retrieving based on a key returns the value stored
# - [x]Successfully returns null for a key that does not exist in the hashtable
# - [x]Successfully handle a collision within the hashtable
# - [x]Successfully retrieve a value from a bucket within the hashtable that has a collision
# - [x]Successfully hash a key to an in-range value
import pytest
from data_structure.hash_table.hashtable import HashTable

def test_instantiate_hash_table():
    ht = HashTable()
    assert ht.size == 1024
    assert ht.buckets == [None] * 1024

def test_return_index_hash():
    # Arrange
    ht = HashTable()
    expected = 64
    # Act
    actual = ht._HashTable__hash('test')
    # Assert
    assert actual == expected

def test_return_similar_index_for_similar_ord_words_hash():
    ht = HashTable()
    assert ht._HashTable__hash('test') == ht._HashTable__hash('etts')

def test_return_diff_index_for_diff_ord_words_hash():
    ht = HashTable()
    assert ht._HashTable__hash('test') != ht._HashTable__hash('eets')

def test_add_key_value():
    # Arrange
    ht = HashTable()
    ht.add("dua",27)
    assert ht._HashTable__hash('dua')

def test_add_to_LL_handle_collision():
    # Arrange
    ht = HashTable()
    ht.add("dua",27)
    ht.add("uad",28)
    assert ht._HashTable__hash('dua') == ht._HashTable__hash('uad')

def test_get_value_for_present_key():
    # Arrange
    ht = HashTable()
    ht.add("dua",27)
    ht.add("uad",28)
    expected =  27
    # Act
    actual = ht.get("dua")
    # Assert
    assert actual == expected

def test_get_none_for_not_present_key():
    ht = HashTable()
    with pytest.raises(KeyError):
        assert ht.get("ahmad")

def test_get_value_in_LL_key():
    # Arrange
    ht = HashTable()
    ht.add("dua",27)
    ht.add("uad",28)
    ht.add("aud",29)
    expected =  29
    # Act
    actual = ht.get("aud")
    # Assert
    assert actual == expected

def test_hashtable_contains_key_value():
    # Arrange
    ht = HashTable()
    ht.add("dua",27)
    ht.add("uad",28)
    ht.add("aud",29)
    expected =  True
    # Act
    actual = ht.contains("aud")
    # Assert
    assert actual == expected

def test_hashtable_remove_key_value():
    # Arrange
    ht = HashTable()
    ht.add("dua",27)
    ht.add("uad",28)
    ht.add("aud",29)
    expected =  False
    ht.remove("aud")
    actual = ht.contains("aud")
    assert actual == expected

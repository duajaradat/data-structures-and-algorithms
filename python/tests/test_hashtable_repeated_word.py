import pytest
from code_challenges.repeated_word.repeated_word import repeated_word
from data_structure.hash_table.hashtable import HashTable

def test_instantiate_hashtable():
    ht = HashTable()
    assert ht

def test_empty_string():
    ht = HashTable()
    assert repeated_word('') == None

def test_no_repeated_word():
    assert repeated_word('hello world') == None

def test_no_repeated_word_2():
    assert repeated_word('aaaaaaaaa') == None

def test_repeated_word():
    # Arrange
    string = "Once upon a time, there was a brave princess who..."
    assert repeated_word(string) == 'a'

def test_repeated_word_2():
    # Arrange
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    assert repeated_word(string) == 'it'

def test_repeated_word_2():
    # Arrange
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    assert repeated_word(string) == 'it'


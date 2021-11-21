from data_structure.hash_table.hashtable import HashTable
def repeated_word(string):
    """
    Given a string, find the first repeated word.

    Parameters
    Arguments: text (string)

    Returns: string
    """
    if not string:
        return None

    ht = HashTable()
    string = string.lower()
    words = string.split()
    for word in words:
        if ht.contains(word):
            return word
        else:
            ht.add(word,word)
    return None
# "Once upon a time, there was a brave princess who"

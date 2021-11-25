from data_structure.hash_table.hashtable import HashTable

def left_join(hashmap_one :HashTable, hashmap_two :HashTable):
    """
    Left join two hashmaps
    """
    output = []

    if  not len(hashmap_one.buckets)  and not len(hashmap_two.buckets) :
        return []

    for i in range(len(hashmap_one.buckets)):
        if hashmap_one.buckets[i]:
            if hashmap_two.contains(hashmap_one.buckets[i].head.value[0]):
                output.append([hashmap_one.buckets[i].head.value[0], hashmap_one.buckets[i].head.value[1], hashmap_two.buckets[i].head.value[1]])
            else:
                output.append([hashmap_one.buckets[i].head.value[0], hashmap_one.buckets[i].head.value[1], None])

    return output

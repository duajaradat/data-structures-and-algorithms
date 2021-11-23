from data_structure.hash_table.hashtable import HashTable


def common_values(tree_one,tree_two):

    if not tree_one.root  or not tree_two.root :
        return None

    hashtable = HashTable()
    result_values = []

    def walk_one(node):
        nonlocal hashtable
        if node:
            hashtable.add(str(node.data),node.data)
            walk_one(node.left)
            walk_one(node.right)

    walk_one(tree_one.root)

    def walk_two(node):
        nonlocal hashtable
        nonlocal result_values
        if node:
            if hashtable.contains(str(node.data)):
                result_values.append(node.data)
            walk_two(node.left)
            walk_two(node.right)

    walk_two(tree_two.root)

    print(result_values)


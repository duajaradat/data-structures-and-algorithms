from data_structure.hash_table.hashtable import HashTable


def common_values(tree_one ,tree_two):

    if not tree_one.root  or not tree_two.root :
        return None

    hashtable = HashTable()
    result_values = []

    def walk_one(node):

        if node:
            hashtable.add(str(node.data),node.data)
        if node.left:
            walk_one(node.left)
        if node.right:
            walk_one(node.right)


    walk_one(tree_one.root)

    def walk_two(node):

        if node:
            if hashtable.contains(str(node.data)):
                result_values.append(node.data)
        if node.left:
            walk_two(node.left)
        if node.right:
            walk_two(node.right)

        return result_values

    return walk_two(tree_two.root)



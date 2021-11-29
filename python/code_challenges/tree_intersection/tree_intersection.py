from data_structure.hash_table.hashtable import HashTable


def common_values(tree_one ,tree_two):
    """
    function to find the common values between two trees
    Args : tree_one  and tree_two (binary tree)
    Returns : list of common values
    """
    if not tree_one.root  or not tree_two.root :
        return None

    hashtable = HashTable()
    result_values = []

    def walk_one(node):
        """
        function to walk through the tree and add the values to the hashtable
        Args : node (root of the tree)
        Returns : None
        """

        if node:
            hashtable.add(str(node.data),node.data)
        if node.left:
            walk_one(node.left)
        if node.right:
            walk_one(node.right)


    walk_one(tree_one.root)

    def walk_two(node):
        """
        function to walk through the tree and check if the values are in the hashtable
        Args : node (node of the tree)
        Returns : list of common values
        """

        if node:
            if hashtable.contains(str(node.data)):
                result_values.append(node.data)
        if node.left:
            walk_two(node.left)
        if node.right:
            walk_two(node.right)

        return result_values

    return walk_two(tree_two.root)



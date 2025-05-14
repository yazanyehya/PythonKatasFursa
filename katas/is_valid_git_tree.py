
def is_valid_git_tree(tree_map):
    parents = set()
    children = set()
    for parent, children_list in tree_map.items():
        parents.add(parent)
        for child in children_list:
            children.add(child)

    roots = parents - children
    if len(roots) != 1:
        return False

    visited = set()
    visiting = set()
    root = next(iter(roots))

    def dfs(node):
        if node in visiting:
            return False
        if node in visited:
            return True

        visiting.add(node)
        for neighbor in tree_map.get(node,[]):
            if not dfs(neighbor):
                return False
        visiting.remove(node)
        visited.add(node)
        return True

    if not dfs(root):
        return False
    all_nodes = parents.union(children)


    return visited == all_nodes



if __name__ == '__main__':
    valid_tree = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],
        "D": []
    }

    invalid_tree = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]  # cycle
    }

    print(f"Is valid tree: {is_valid_git_tree(valid_tree)}")  # Should be True
    print(f"Is valid tree: {is_valid_git_tree(invalid_tree)}")  # Should be False
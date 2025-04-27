def flatten_list(nested_list):
    flatter_list = []
    for item in nested_list:
        if isinstance(item,list):
            flatter_list.extend(flatten_list(item))
        else:
            flatter_list.append(item)

    return flatter_list


if __name__ == '__main__':
    nested_list = [
        1,
        [2, 3],
        [4, [5, 6]],
        7
    ]

    flat_list = flatten_list(nested_list)

    print(f"Flattened list: {flat_list}")  # Should be [1, 2, 3, 4, 5, 6, 7]
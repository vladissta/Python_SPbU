def query_w_overlaps_searcher(query: str, string: str):

    print(f'Search "{query}" in "{string}"')

    indexes = []
    start = 0

    while True:
        found_position = string.find(query, start)
        if found_position == -1:
            break
        indexes.append(found_position)
        start = found_position + 1

    print(f'Query hits were found at {indexes=}')

    return indexes


if __name__ == '__main__':
    assert query_w_overlaps_searcher('bcb', 'abcbcbcbcaaabcb') == [1, 3, 5, 12]

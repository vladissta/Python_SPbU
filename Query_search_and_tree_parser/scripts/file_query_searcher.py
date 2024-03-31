from query_searcher import query_w_overlaps_searcher
from tabulate import tabulate


def query_in_file_searcher(query: str, file: str):
    query_len = len(query)
    table = []

    with open(file, 'r') as f:
        for n_line, line in enumerate(f):
            indexes = query_w_overlaps_searcher(query, line)

            if not indexes:
                continue

            for idx in indexes:
                start_idx = 0 if idx < 15 else idx - 15
                end_idx = len(line) - 1 if idx + query_len + 14 > len(line) else idx + query_len + 14
                context = line[start_idx:idx], f'\033[92m{query}\033[0m', line[idx + query_len:end_idx]

                table.append(
                    [n_line + 1, idx + 1,
                     ''.join([line[start_idx:idx],
                              f'\033[92m{query}\033[0m',
                              line[idx + query_len:end_idx]])])

    print(tabulate(table, headers=['Line', 'Position', 'Context'], tablefmt='orgtbl'))


if __name__ == '__main__':
    query_in_file_searcher('AGCC', '../test_data/multifasta.fa')

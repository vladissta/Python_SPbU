def alphabet_stat_fun_maker(alphabet: str):
    """
    :param alphabet: alphabet in the following format: "ABCDabcd123" (i.e written together)
    :return: Function that prints percentage of alphabet symbols usage in given sequence
    """
    alphabet_set = set(alphabet)
    alphabet_stat_dict = dict(zip(alphabet_set, [0] * len(alphabet)))

    def alphabet_stat(seq: str):
        """
        Prints percentage of alphabet symbols usage in given sequence + prints pretty text barplot
        :param seq: Sequence to count statistics of symbols usage
        :return: None
        """
        if not set(seq).issubset(alphabet_set):
            raise ValueError("Wrong alphabet of inputted sequence!")

        length_of_seq = len(seq)
        for symbol in seq:
            alphabet_stat_dict[symbol] += 1 / length_of_seq
        for key, value in alphabet_stat_dict.items():
            print(f'{key}: {value:.2%}')
            print("=" * int(value * 50))

    return alphabet_stat


if __name__ == '__main__':
    alpha_counter_DNA = alphabet_stat_fun_maker('AGCT')
    alpha_counter_DNA('AGCGTCGTGTGG')
    print()

    alpha_counter_RNA = alphabet_stat_fun_maker('AGCU')
    alpha_counter_RNA('AUAUGGCGAACGU')
    print()

    try:
        alpha_counter_RNA = alphabet_stat_fun_maker('AGCU')
        alpha_counter_RNA('AGCGTCGTGTGG')
    except ValueError:
        print('Expected error was raised')

    print()

    try:
        alpha_counter_RNA = alphabet_stat_fun_maker('AGCU')
        alpha_counter_RNA('AUAUAUAU')
    except ValueError:
        print('Unexpected error was raised !!!')

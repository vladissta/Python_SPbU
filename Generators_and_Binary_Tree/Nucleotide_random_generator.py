from numpy.random import normal
import random


def nucleotide_random_generator(A_probability: float = 0.25,
                                G_probability: float = 0.25,
                                C_probability: float = 0.25,
                                T_probability: float = 0.25):
    while True:
        yield random.choices(['A', 'G', 'C', 'T'],
                             weights=[A_probability, G_probability,
                                      C_probability, T_probability])


def random_sequence_generator(n_sequences: int, mu: int, sigma: int, char_generator):
    length = int(normal(mu, sigma))

    for _ in range(n_sequences):
        seq_list = []
        for _ in range(length):
            seq_list.append(*next(char_generator))

        yield ''.join(seq_list)


if __name__ == '__main__':
    nucl_gen = nucleotide_random_generator(0.2, 0.3, 0.3, 0.2)

    seq_gen = random_sequence_generator(2, 5, 3, nucl_gen)

    for i in seq_gen:
        print(i)

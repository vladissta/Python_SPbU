from dataclasses import dataclass


@dataclass
class FastaRecord:
    name: str
    sequnce: str


def fasta_generator(multifasta_file):
    with open(multifasta_file, 'r') as multifasta:
        name = None
        seq = []

        for line in multifasta:
            if line.startswith('>'):
                if name:
                    yield FastaRecord(name, ''.join(seq))
                    seq = []
                name = line.lstrip('>').split(maxsplit=1)[0]
            else:
                seq.append(line)

        if name:
            yield FastaRecord(name, ''.join(seq))


if __name__ == '__main__':
    fasta_gen = fasta_generator('../data/multifasta.fa')

    for fa in fasta_gen:
        print(fa.name)
        print(fa.sequnce)

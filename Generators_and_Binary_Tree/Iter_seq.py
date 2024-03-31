from HW4.Seq_classes import Sequence, DNA, RNA, Protein


class Iterable_sequence(Sequence):

    def __iter__(self):
        # return (nuc for nuc in self.sequence)
        return iter(self.sequence)


class Iterable_DNA(DNA, Iterable_sequence):
    pass


class Iterable_RNA(RNA, Iterable_sequence):
    pass


class Iterable_Protein(Protein, Iterable_sequence):
    pass


if __name__ == '__main__':
    seq = Iterable_DNA('dna', 'AGCT')

    for nuc in seq:
        print(nuc)

    compl_dna = seq.compliment_seq()

    print([nucl for nucl in compl_dna])

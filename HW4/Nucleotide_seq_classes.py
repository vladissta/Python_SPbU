from abc import ABC, abstractmethod


class NucleotideSequence(ABC):

    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    @property
    @abstractmethod
    def _alphabet_str(self) -> str:
        """
        Alphabet of nucleotide sequence should be defined!
        """
        pass

    @property
    def sequence(self) -> str:
        """
        Gets the sequence attribute of an instance
        :return:
        """
        return self._sequence

    @sequence.setter
    def sequence(self, seq: str):
        """
        Sets the sequence attribute of an instance
        :param seq: sequence of instance
        :return:
        """
        # checking if DNA/RNA class got correct DNA/RNA sequence respectively
        if set(self._alphabet_str) != set(seq):
            raise ValueError(f'Inputted sequence is not {self.__class__.__name__}')
        self._sequence = seq.upper()

    def compliment_seq(self):
        """
        :return: compliment sequence (not reversed!)
        """
        trans_dict = str.maketrans(self._alphabet_str, self._alphabet_str[::-1])
        return self._sequence.translate(trans_dict)

    @property
    def nucleotides_fraction(self) -> dict:
        """
        :return: dictionary with nucleotide as a keys and corresponding fractions as a values
        """
        frac_dict = dict(zip(self._alphabet_str, [0, 0, 0, 0]))
        for nucl in self.sequence:
            frac_dict[nucl] += 1 / len(self)

        return frac_dict

    def get_one_stranded_molecular_weight(self):
        """
        Prints the average molecular weight of nucleotide sequence
        :return: None
        """
        nucleotide_molecular_weight = 330
        print(f'Molecular weight of the {self.name} is {nucleotide_molecular_weight * len(self)} g/mol')


class RNA(NucleotideSequence):
    _alphabet_str = 'AGCU'

    # Dictionary for translation RNA -> Protein
    _codon_table = {
        'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
        'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
        'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
        'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
        'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
        'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
        'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
        'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
        'UAC': 'Y', 'UAU': 'Y', 'UAA': None, 'UAG': None,
        'UGC': 'C', 'UGU': 'C', 'UGA': None, 'UGG': 'W',
    }

    def translate(self):
        """
        Translates RNA sequence to aminoacid sequence
        :return: aminoacid sequence
        """
        if not len(self) % 3 == 0:  # checks whether the sequence can be translated (its length is  multiple of 3)
            raise ValueError(f'Sequence length is not a multiple of 3')

        protein = []
        for nucl_num in range(0, len(self.sequence), 3):
            # appending aminoacids of corresponding codons into the list
            protein.append(self._codon_table[self.sequence[nucl_num:nucl_num + 3]])
        return ''.join(protein)


class DNA(NucleotideSequence):
    _alphabet_str = 'AGCT'

    def transcript(self, name_of_rna: str = 'New RNA') -> RNA:
        """
        Transcripts  DNA into RNA
        [!] The DNA sequence is supposed to be on the coding strand
        :param name_of_rna: Name of the new RNA sequence
        :return: RNA object
        """
        trans_dict = str.maketrans(self._alphabet_str, 'AGCU')
        return RNA(name_of_rna, self.sequence.translate(trans_dict))


if __name__ == '__main__':
    print('Small tests:\n')

    dna = DNA('dna', 'CAGCTAGCTAGCTTTGCTAGC')

    rna = dna.transcript()
    print(rna.translate())

    print(rna.nucleotides_fraction)

    dna.get_one_stranded_molecular_weight()

    try:
        dna2 = DNA('dna2', 'AUUGGCGC')
    except ValueError:
        print('Expected error 1 was raised')

    try:
        rna2 = RNA('rna2', 'auaugucgcg')
        print(rna2.translate())
    except ValueError:
        print('Expected error 2 was raised')

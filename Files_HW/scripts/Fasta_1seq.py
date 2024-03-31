def read_fasta_record(file_fasta):
    with open(file_fasta, 'r') as fasta:
        print('Sequence Name:', fasta.readline().lstrip('>').split(maxsplit=1)[0])

        print('Sequence:')
        while (line := fasta.readline()) != '':
            print(line, end='')


if __name__ == '__main__':
    read_fasta_record('../data/fimA.fasta')

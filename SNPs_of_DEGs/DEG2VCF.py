import re

DEG_FILE = 'data/deg_chr22.tsv'
VCF_FILE = 'data/test.chr22.ann.vcf'
OUTPUT_FILE = 'output.vcf'

filtered_genes = []

with open(DEG_FILE, 'r') as deg_file:
    deg_file.readline()

    for line in deg_file:
        gene_data = line.split('\t')

        if float(gene_data[1]) < 0.05 and abs(float(gene_data[2])) > 1:
            filtered_genes.append(gene_data[0])

genes_pattern = '|'.join(filtered_genes)

with open(VCF_FILE, 'r') as vcf_file, open('output.vcf', 'w') as output_file:
    for line in vcf_file:
        if line.startswith('#'):
            continue

        INFO = line.split()[7]

        if re.search(genes_pattern, INFO):
            print(line, file=output_file)

#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('vcf_file', type=str)
parser.add_argument('step', type=int)
parser.add_argument('output_file', type=str)
args = parser.parse_args()

with open(args.vcf_file, 'r') as vcf_file, open(args.output_file, 'w') as output_file:
    output_file.write('contig\tsegment_coordinate\tnumber_of_substitutions\n')

    current_contig = None
    current_position = 0
    substitutions = 0

    for line in vcf_file:
        if line.startswith('#'):
            continue

        fields = line.strip().split('\t')
        contig = fields[0]
        position = int(fields[1])

        # If we've reached a new contig or a new segment, write the previous segment to the output file
        if contig != current_contig or position - current_position > args.step:
            if current_contig is not None:
                output_file.write(f'{current_contig}\t{current_position}\t{substitutions}\n')

            current_contig = contig
            current_position = position
            substitutions = 0

        substitutions += 1

    if current_contig is not None:
        output_file.write(f'{current_contig}\t{current_position}\t{substitutions}\n')

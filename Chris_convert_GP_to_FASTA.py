__author__ = 'Chris Doan'

import re

input_file = open('O104_H4_GP.txt', "r")
output_file = open('O104_H4_GP.out.txt', "w")
version = definition = amino_acid = None
for line in input_file:
    version_re = re.search(r'^VERSION\s*(\w*.\d)', line)
    if version_re:
        version = version_re.group(1),
        version = '>' + ''.join(version) + ' ' '\n'
        output_file.writelines(version)
    definition_re = re.search(r'^DEFINITION\s*(\w*[:\s*]\w*)|\s{12}.*\]\.$', line)
    if definition_re:
        definition = line[12:]
        output_file.writelines(definition)
        output_file.writelines('\n')
    amino_acid_re = re.search(r'^\s{5,8}\d{1,4}\s(\w.*)', line)
    if amino_acid_re:
        amino_acid = amino_acid_re.group(1)
        amino_acid = amino_acid.upper()
        output_file.writelines(amino_acid)
        output_file.writelines('\n')

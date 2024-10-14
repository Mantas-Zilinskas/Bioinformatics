from os import listdir
from os.path import isfile, join
from sequence_generator import generate_reverse_compliment
from codon_funcs import find_stop_start, to_amino_acids, count_codon_frequency, count_dicodon_frequency, cosine_similarity
import sys



mypath = sys.argv[1]
file_names = [f for f in listdir(mypath) if isfile(join(mypath, f))]
file_names = [f for f in file_names if f.split('.')[-1] == "fasta" ]
reverse_compliment_sequences = []
sequences = []
organism_names = []

for file in file_names:
    f = open(mypath + "\\" + file, 'r')
    content = generate_reverse_compliment(f)
    ls = content.split("\n")
    ls = ls[1:]
    content = "".join(ls)
    genes = find_stop_start(content)
    aminos = to_amino_acids(content, genes)
    reverse_compliment_sequences.append(aminos)
    f.close()

for file in file_names:
    f = open(mypath + "\\" + file, 'r')
    content = f.read()
    ls = content.split("\n")
    organism_names.append(ls[0])
    ls = ls[1:]
    content = "".join(ls)
    genes = find_stop_start(content)
    aminos = to_amino_acids(content, genes)
    sequences.append(aminos)
    f.close()

codon_freqs = []
for sequence in sequences:
    codon_freqs.append(count_codon_frequency(sequence))

dicodon_freqs = []
for sequence in sequences:
    dicodon_freqs.append(count_dicodon_frequency(sequence))


result_file = open(mypath + "\\" + "codon_distance_matrix.txt", 'w') 
result_file.write(f"{len(codon_freqs)} \n")
for i in range(len(codon_freqs)):
    for j in range(len(codon_freqs)):
        result_file.write(f"{cosine_similarity(codon_freqs[i], codon_freqs[j])} ")
    result_file.write(organism_names[i] + "\n")


diresult_file = open(mypath + "\\" + "dicodon_distance_matrix.txt", 'w') 
diresult_file.write(f"{len(dicodon_freqs)} \n")
for i in range(len(dicodon_freqs)):
    for j in range(len(dicodon_freqs)):
        diresult_file.write(f"{cosine_similarity(dicodon_freqs[i], dicodon_freqs[j])} ")
    diresult_file.write(organism_names[i] + "\n")





    


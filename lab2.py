import os
import sys
from aminos import Aminos


def to_amino_acids(dna, genes):
    amino_acids = []
    amino_arr = []
    for gene in genes:
        for i in range(gene[0], gene[1] + 3, 3):
            amino_arr.append(Aminos[dna[i:i+3]])
    amino_acids = ''.join(amino_arr)
    return amino_acids

def count_codon_frequency(amino_acids):
    freq = {}
    length = len(amino_acids)
    for amino in amino_acids:
        if freq.get(amino) == None:
            freq[amino] = 1
        else:
            freq[amino] = freq[amino] + 1

    for thing in freq:
        freq[thing] = '%.5f'%(freq[thing]/length)
    
    return freq 

def count_dicodon_frequency(amino_acids):
    freq = {}
    length = len(amino_acids)
    for i in range(0, len(amino_acids), 2):
        if freq.get(amino_acids[i:i+2]) == None:
            if len(amino_acids[i:i+2]) == 1:
                continue
            freq[amino_acids[i:i+2]] = 1
        else:
            freq[amino_acids[i:i+2]] = freq[amino_acids[i:i+2]] + 1

    for thing in freq:
        freq[thing] = '%.5f'%(freq[thing]/length)
    
    return freq

def find_stop_start(path):
    file_name = os.path.basename(path).split('/')[-1].split('.')[-2]

    file = open(path, "r")
    name = file.readline()
    content = file.read()
    content = ''.join(content.split('\n'))


    flag = False
    genes = []
    start = None

    i = 0
    while(i < len(content) - 3): 
        match content[i:i+3]:
            case "ATG":
                if flag == False:
                   flag = True
                   start = i

            case "TAG":
                if flag:
                    flag = False
                    genes.append((start, i))

            case "TAA":
                if flag:
                    flag = False
                    genes.append((start, i))
            case "TGA":
                if flag:
                    flag = False
                    genes.append((start, i))
            case _:
                None
        if flag:
            i += 3
        else:
            i += 1

    genes = [i for i in genes if (i[1] - i[0]) > 100]
    return genes



    
    
   
    
path = sys.argv[1]

find_stop_start(path)
print(count_dicodon_frequency("ABCDEFGGGAADA"))




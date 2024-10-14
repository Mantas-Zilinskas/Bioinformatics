import os
import sys
from aminos import Aminos


def evaluate_distance(open_frame1, open_frame2, tolerance = 0):
    primary = None
    secondary = None

    matches = 0

    if len(open_frame1) < len(open_frame2):
        primary = open_frame1
        secondary = open_frame2
    else:
        secondary = open_frame1
        primary = open_frame2

    i = 0
    j = 0
    skips = 0
    while(len(primary) > i and len(secondary) > j):
        # print(f"{i}  {j}  {matches}")
        if(skips > 0):
            flag = False
            for l in range(skips):
                if(primary[i] == secondary[j - (l + 1)]):
                    matches += 1
                    i += 1
                    j -= l
                    flag = True
                    skips = 0
                    break
            if flag: 
                continue

        if(primary[i] == secondary[j]):
            matches += 1
            i += 1
            j += 1
            continue
        else:
            for l in range(tolerance):
                if len(secondary) == (j + l + 1):
                    skips += 1 
                    break
                if primary[i] == secondary[j + (l + 1)]:
                    matches += 1
                    j += (l + 1)
                    break
                if l + 1 == tolerance and skips < tolerance:
                    skips += 1 
        
        i += 1
        j += 1 
           
    return 1 - matches / len(primary)
               
           

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
    amino_acids = "".join(amino_acids.split("*"))
    length = len(amino_acids)
    for amino in amino_acids:
        if freq.get(amino) == None:
            freq[amino] = 1
        else:
            freq[amino] = freq[amino] + 1

    for key in freq:
        freq[key] = '%.5f'%(freq[key]/length)
    
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

def find_stop_start(content):

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




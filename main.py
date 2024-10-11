from os import listdir
from os.path import isfile, join
from sequence_generator import generate_reverse_compliment
import sys



mypath = sys.argv[1]
file_names = [f for f in listdir(mypath) if isfile(join(mypath, f))]
reverse_compliment_file_contents = []
file_contents = []

for file in file_names:
    f = open(mypath + "\\" + file, 'r')
    content = f.read()
    ls = content.split("\n")
    ls = ls[1:]
    reverse_compliment_file_contents.append("".join(ls))
    f.close()

for file in file_names:
    f = open(mypath + "\\" + file, 'r')
    content = f.read()
    ls = content.split("\n")
    ls = ls[1:]
    file_contents.append("".join(ls))
    f.close()
    

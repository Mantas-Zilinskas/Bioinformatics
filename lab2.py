import os
import sys


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
    print(genes)
    
    
   
    
path = sys.argv[1]

find_stop_start(path)





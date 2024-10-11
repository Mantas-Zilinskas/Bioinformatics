import os
import sys


def generate_reverse_compliment(file):

    name = file.readline()
    content = file.read()
    content = content[::-1]
    content = "".join(content.splitlines())

    content_reverse_compliment = []
    counter = 0
    for letter in content:
        if counter == 70:
            content_reverse_compliment.append("\n")
            counter = 0
        
        match letter:
            case 'A':
                 content_reverse_compliment.append("T")
            case 'T':
                 content_reverse_compliment.append("A")
            case 'C':
                 content_reverse_compliment.append("G")
            case 'G':
                 content_reverse_compliment.append("C")
            case _:
                  raise Exception("Inpropper input")
        
        counter += 1
    
    return name + "".join(content_reverse_compliment)

    








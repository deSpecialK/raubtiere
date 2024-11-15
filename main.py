# Project Raubtiere
#
# Authors: @anne; @emil; @Konstantin; @Karsten

import sys

def file2array (filename):
    list = []

    with open (filename, "r") as file:
        for line in file:
            list.append(line)
    
    return list


    

#Funktion zum Vergleichen zweier Listen
def compare_lists(list1, list2):
    #vergleich beide Listen und schreibt eine Liste aller Uebereinstimmungen in die Variable common
    common = list(set(list1) & set(list2))
    #Gibt die Variable common zurueck
    return common

list1 = file2array(sys.argv[1])
list2 = file2array(sys.argv[2])
for element in (compare_lists(list1, list2)):
    print (element.strip())


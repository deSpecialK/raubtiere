# Project Raubtiere
#
# Authors: @anne; @emil; @Konstantin; @Karsten

import sys

def file2array (filename=sys.argv[1]):
    list = []

    with open (filename, r, ) as file:
        for line in file:
            list.add(line)
    
    return list


    

#Funktion zum Vergleichen zweier Listen
def compare_lists(list1, list2):
    #vergleich beide Listen und schreibt eine Liste aller Uebereinstimmungen in die Variable common
    common = list(set(list1) & set(list2))
    #Gibt die Variable common zurueck
    return common

#list1 = 
#list2 = 
compare_lists(list1, list2)


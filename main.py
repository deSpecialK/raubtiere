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

#function to find out differences between two lists
def differences_lists(list1, list2):
    # Convert lists to sets, substract them
    diff = list(set(list1) - set(list2))
    
    # Return differences
    return diff

list1 = file2array(sys.argv[1])
list2 = file2array(sys.argv[2])

# Schleife
for element in (compare_lists(list1, list2)):
    print (element.strip())

#for element in (differences_lists(list1, list2)):
    #print (element.strip())
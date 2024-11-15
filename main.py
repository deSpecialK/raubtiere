# Project Raubtiere
#
# Authors: @anne; @emil; @Konstantin; @Karsten


#Funktion zum Vergleichen zweier Listen
def compare_lists(list1, list2):
    #vergleich beide Listen und schreibt eine Liste aller Uebereinstimmungen in die Variable common
    common = list(set(list1) & set(list2))
    #Gibt die Variable common zurueck
    return common

#list1 = 
#list2 = 
compare_lists(list1, list2)


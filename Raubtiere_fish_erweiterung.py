# Project Raubtiere
#
# Authors: @anne; @emil; @Konstantin; @Karsten

with open('List_fish_1.txt', 'r') as file1:
    fish_list_1 = set(line.strip() for line in file1)

with open('List_fish_2.txt', 'r') as file2:
    fish_list_2 = set(line.strip() for line in file2)

# Finde die übereinstimmenden Namen
common_fish = fish_list_1.intersection(fish_list_2)

# Ergebnisse in einer neuen Datei speichern
if common_fish:
    print("Die übereinstimmenden Fische sind:")
    for fish in sorted(common_fish):
        print(fish)
else:
    print("Es wurden keine übereinstimmenden Fische gefunden.")

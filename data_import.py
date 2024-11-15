import pandas as pd 
list1_df = pd.DataFrame("mallorca.txt")
list1_df.to_csv('list1.csv', index=False, header=False)
list1_df = pd.read_csv("list1.csv")

list2_df = pd.DataFrame("predator.txt")
list2_df.to_csv('list2.csv', index=False, header=False)
list2_df = pd.read_csv("list2.csv")

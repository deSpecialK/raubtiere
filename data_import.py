import pandas as pd 
list1_df = pd.DataFrame("list1.txt")
list1_df.to_csv('my_csv.csv', index=False, header=False)
list1_df = pd.read_csv("list1.csv")

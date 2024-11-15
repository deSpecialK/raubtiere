import pandas as pd 
my_df = pd.DataFrame("list1")
my_df.to_csv('my_csv.csv', index=False, header=False)


import pandas as pd

calorie = [100,120,140]

series = pd.Series(calorie,index = ['Day 1','Day 2' ,'Day 3'])
print(series)

print("\n After adding extra calories to Day 3 \n")

series.loc['Day 3'] += 100
print(series)
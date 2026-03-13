# Pandas
import pandas as sd

df = sd.read_csv('Sample.csv')

print("The dataset: ")
print(df.head())   #Prints the whole data

print("Dataset Information: ")
print(df.info())  #Displays the basic information

print("Convert age to float numbers: ")
df[" Age"] = (df[" Age"].astype(float))    # Converts age to floating numbers
print(df)

print("Columns in dataset: ")
print(df.columns)          #Display Column names

print("Average of age: ")
group = df.groupby(" Age")
print(group)
print(group[" Age"].mean())    #Displays the mean of datas
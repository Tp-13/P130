from os import access
import pandas as pd
import csv

df = pd.read_csv("final.csv")
print(df.shape)
print(df.columns)
df.drop(["1", "Distance1", "Mass1", "Radius1", "Luminosity", "2"], axis=1, inplace=True)
print(df)

df.to_csv("final_output.csv")
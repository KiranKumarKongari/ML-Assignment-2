import matplotlib.pyplot as plt
import pandas as pd

#df is a dataframe that we load the csv data read in from the URL into
df = pd.read_csv("C:\Users\Kiran Kumar Kongari\Downloads\data.csv", index_col=0)

df.head()

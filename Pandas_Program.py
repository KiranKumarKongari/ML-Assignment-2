# imported packages
import pandas as pd
import matplotlib.pyplot as plt

# 1. df is a dataframe that we load the csv data read in from the URL into.
df = pd.read_csv("C:/Users/Kiran Kumar Kongari/Downloads/data.csv")
print("\nThe Dataframe is : \n", df)

# 2. Showing the basic statistical description about the data
print("\nThe basic statistical description about the data is : \n", df.describe())

# 3. Checking the data has null values and displaying the resultant rows.
y = df[df.isna().any(axis=1)]
print('\n', y)

# a. Replacing the null values with the mean
df['Duration'] = df['Duration'].fillna(df['Duration'].mean())
df['Pulse'] = df['Pulse'].fillna(df['Pulse'].mean())
df['Maxpulse'] = df['Maxpulse'].fillna(df['Maxpulse'].mean())
df['Calories'] = df['Calories'].fillna(df['Calories'].mean())

# Verifying the dataframe again for null values
f = df[df.isna().any(axis=1)]
print('\n', f)

# 4. Select at least two columns and aggregate the data using: min, max, count, mean.
# Selected 2 columns Duration and Pulse and performed the aggregation using: min, max, count, mean
result = df.groupby('Duration').agg({'Pulse': ['min', 'max', 'count', 'mean']})
print(result)

# 5. Filter the dataframe to select the rows with calories values between 500 and 1000.
newdf = df[df['Calories'].between(500, 1000, inclusive='both')]
print("\nrows with calories values between 500 and 1000 are : \n", newdf)

# 6. Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
newdf1 = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]
print("\nrows with calories values > 500 and pulse < 100 are : \n", newdf1)

# 7. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.
df_modified = df[['Duration', 'Pulse', 'Calories']].copy()
print("\nNew dataframe after ignoring Maxpulse column is : \n", df_modified)

# 8. Delete the “Maxpulse” column from the main df dataframe
df = df.drop('Maxpulse', axis=1)
print("\nDataframe df after removing Maxpulse column : \n", df)

# 9. Convert the datatype of Calories column to int datatype.
df["Calories"] = df["Calories"].astype(int)
print("\nDatatypes of the Calories column after converting to int datatype : \n", df.dtypes)

# 10. Using pandas create a scatter plot for the two columns (Duration and Calories).
df.plot.scatter(x='Duration', y='Calories', s=100)
plt.show()






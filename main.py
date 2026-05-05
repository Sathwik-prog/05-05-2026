import pandas as pd
import numpy as np

data = {
    "Id": [1, 2, 3, 4],
    "Name": ["Pankaj", "Meghna", "David", "Lisa"],
    "Role": ["CEO", np.nan, np.nan, np.nan],
    "Salary": [100, 200, np.nan, np.nan]
}

df = pd.DataFrame(data)

print(df.head(2))
print(df.tail(2))

print(df.isnull().sum())
print(df.info())

df_rows_dropped = df.dropna()
print(df_rows_dropped)

df_cols_dropped = df.dropna(axis=1)
print(df_cols_dropped)

df["Salary"].fillna(300, inplace=True)
df["Role"].fillna("CEO", inplace=True)

print(df)
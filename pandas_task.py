import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Check columns
print("Columns:", df.columns)

# Show first rows
print(df.head())

# Info
print(df.info())

# Work with 'myvar'
print("\nColumn data:")
print(df["myvar"])

# Filter values (example > 10)
filtered = df[df["myvar"] > 10]
print("\nFiltered Data:")
print(filtered)

# Add new column
df["myvar_plus_5"] = df["myvar"] + 5

# Handle missing values
df.fillna(0, inplace=True)

# Sort data
df = df.sort_values(by="myvar")

# Basic statistics
print("\nMean of myvar:", df["myvar"].mean())

# Save output
df.to_csv("output.csv", index=False)

print("\nDone - output saved as output.csv")
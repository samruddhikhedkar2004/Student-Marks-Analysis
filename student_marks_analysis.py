import pandas as pd

# Load the dataset
df = pd.read_csv("students.csv")

# Display basic info
print("Basic Data Info:")
print(df.info())
print()

# Display first 5 rows
print("First 5 Entries:")
print(df.head())
print()

# Find average marks
print("Average Marks in Each Subject:")
print(df[['Math', 'Science', 'English']].mean())
print()

# Find topper
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
topper = df.loc[df['Total'].idxmax()]
print(f"Topper: {topper['Name']} with total {topper['Total']} marks")
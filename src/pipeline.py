import pandas as pd

# Read the CSV file
df = pd.read_csv("data/jobs.csv")

print("Original data:")
print(df)
print(f"\nRows before cleaning: {len(df)}")

# Count duplicates before removing them
duplicate_count = df.duplicated(subset=["job_id"]).sum()

# Basic cleaning
df["title"] = df["title"].str.strip().str.title()
df["company"] = df["company"].str.strip()
df["location"] = df["location"].str.strip().str.title()
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["posted_date"] = pd.to_datetime(df["posted_date"], errors="coerce")

# Handle missing values
df["title"] = df["title"].fillna("Unknown")
df["company"] = df["company"].fillna("Unknown")
df["location"] = df["location"].fillna("Unknown")

# Remove duplicate job IDs
df = df.drop_duplicates(subset=["job_id"])

# Remove rows where salary is missing
df = df.dropna(subset=["salary"])

# Save cleaned data
df.to_csv("data/cleaned_jobs.csv", index=False)

print("\nCleaned data:")
print(df)

print(f"\nRows after cleaning: {len(df)}")
print(f"Duplicate job_ids removed: {duplicate_count}")
print("\nNull values by column:")
print(df.isnull().sum())

print("\nCleaned file saved as data/cleaned_jobs.csv")

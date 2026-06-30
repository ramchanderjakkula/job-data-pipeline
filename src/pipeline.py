import pandas as pd

# Read the CSV file
df = pd.read_csv("data/jobs.csv")

# Show original data
print("Original data:")
print(df)

# Basic cleaning
df["title"] = df["title"].str.strip()
df["company"] = df["company"].str.strip()
df["location"] = df["location"].str.strip()
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["posted_date"] = pd.to_datetime(df["posted_date"], errors="coerce")

# Remove duplicate job IDs
df = df.drop_duplicates(subset=["job_id"])

# Save cleaned data
df.to_csv("data/cleaned_jobs.csv", index=False)

print("\nCleaned data:")
print(df)

print("\nCleaned file saved as data/cleaned_jobs.csv")

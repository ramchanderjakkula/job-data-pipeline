# Job Data Pipeline

A beginner-friendly data engineering project that reads raw job data from a CSV file, cleans it with Python, and writes a transformed output file for analysis.

## Overview

This project demonstrates a simple ETL workflow:

- Extract raw job data from a CSV file
- Transform and clean the data using pandas
- Remove duplicate records
- Handle missing salary values
- Standardize text fields like title, company, and location
- Load the cleaned result into a new CSV file
- Prepare SQL queries for future analysis

## Tech Stack

- Python
- pandas
- SQL
- Git
- GitHub
- VS Code

## Project Structure

```text
job-data-pipeline/
├── data/
│   ├── jobs.csv
│   └── cleaned_jobs.csv
├── src/
│   └── pipeline.py
├── sql/
│   └── analysis.sql
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Run the pipeline

```bash
python src/pipeline.py
```

## Input Data Issues Handled

The pipeline cleans several common data quality problems:

- duplicate job IDs
- missing salary values
- extra whitespace
- inconsistent capitalization

## Output

The pipeline reads raw data from:

```text
data/jobs.csv
```

and writes cleaned data to:

```text
data/cleaned_jobs.csv
```

It also prints:

- row counts before and after cleaning
- number of duplicate records removed
- null counts by column

## Sample SQL Analysis

The `sql/analysis.sql` file includes example queries for:

- listing all job records
- average salary by title
- job counts by location

## Future Improvements

- load data into PostgreSQL
- add automated tests
- schedule pipeline runs

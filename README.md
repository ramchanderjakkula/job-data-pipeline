# Job Data Pipeline
A beginner-friendly data engineering project that reads job data from a CSV file, cleans it with Python, and saves a transformed output file for analysis.
## Overview
This project demonstrates a simple ETL pipeline:
- Extract job data from a raw CSV file
- Transform and clean the data using pandas
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
How to Run
Install dependencies
bash


pip install -r requirements.txt
Run the pipeline
bash


python src/pipeline.py
Output
The pipeline reads raw data from:

text


data/jobs.csv
and writes cleaned data to:

text


data/cleaned_jobs.csv
Sample SQL Analysis
The SQL file includes example queries for:

listing all job records
average salary by title
job counts by location
Future Improvements
load data into PostgreSQL
add tests
schedule pipeline runs
containerize with Docker
add dashboards
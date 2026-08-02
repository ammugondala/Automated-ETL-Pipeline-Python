# ETL Pipeline Project

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline using Python. It extracts employee data from a CSV file or Azure SQL Database, transforms the data, loads it into a SQLite database, generates reports and visualizations, and can upload reports to Azure Blob Storage.

## Features

- Extract data from CSV
- Optional Azure SQL Database support
- Data cleaning and transformation
- Load data into SQLite
- Generate HTML report
- Generate Excel report
- Create charts using Matplotlib
- Send reports through Email
- Azure Blob Storage upload support
- Logging
- Environment variable configuration using `.env`

## Technologies Used

- Python
- Pandas
- SQLite
- Matplotlib
- OpenPyXL
- python-dotenv
- Azure Storage Blob SDK
- SQLAlchemy
- PyODBC

## Project Structure

```
ETLProject/
│
├── data/
├── etl/
├── reports/
├── logs/
├── .env
├── requirements.txt
├── README.md
└── run_etl.py
```

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python run_etl.py
```

## Output

The project generates:

- SQLite Database
- HTML Report
- Excel Report
- Charts
- Logs
- Email Notification
- Azure Blob Upload (optional)

## Author

Amrutha varshini Gondala
B.Tech CSE
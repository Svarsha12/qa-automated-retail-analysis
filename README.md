# QA-Automated-Retail-Data-Analysis #

# Overview

This project demonstrates a complete data pipeline that blends QA automation, data governance, analytics, and interactive dashboards using a realistic retail sales dataset.
It showcases how you can ensure data quality, perforrm validation using pytest, document metadat, and visualize business and QA metrics using Tableau

# Data Source
https://www.kaggle.com/datasets/shandeep777/retail-supply-chain-sales-dataset

# QA Validation

I implemented automated validation rules:

- Order ID Uniqueness
- Null Checks on Critical Columns
- Ship Data must be on/after Order Date

- Results are exported to:
1. reports/validation_report.html
2. governance/steward_issues.csv

# Governance Artifacts

- data_dictionary.csv: Column-level metadat
- steward_issues.csv : Logged QA issues with severity/issues
- lineage.md: Shows end-to-end data flow and governance checks

# Tableau Dashboards
Build us clean_orders.csv and qa_summary.csv, dashboards include:
- Sales by Region, Segment, Category
- QA Pass/Fail Overview (Pie + Table)
- Return Trends and Shipping Delays

# View Dashboard on Tableau Pulic: 
https://public.tableau.com/app/profile/varsha.sharma1882/viz/RetailDataQualityDashboard/RetailSalesDataQuality


# How to Run Locally

- Clone this repo
- Place raw files in data/
- Install dependencies

```
pip install -r requirements.txt

```

- Run tests

```
pytest --html=reports/validation_report.html

```

# Project Highlights

- Combine QA + Analytics + Visualization
- Simulate real-world governance practices
- Public Tableau dashboard for showcasing
- Designed to help transition into data governance/data analyst roles

# Future Enhancements

- Add ML model for sales forecasting
- Create parameterized QA test suite
- Integrate with a data catalog or metadata store

# Helpful tip for create and activate a virtual environment
```python -m venv venv```
```
source venv/bin/activate
```


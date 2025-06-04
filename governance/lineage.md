# Data Lineage - QA-Automated-Retail-Analysis Project

## 1. Data Sources
- `retail_order.csv` — Raw sales and order data
- `calendar_table.csv` — Time dimension for enriching orders

## 2. ETL / Processing (via Python)
- `data_loader.py`: Loads and parses the raw data
- `validation.py`: Applies QA checks (nulls, duplicates, ship dates)
- `visualize.py`: Generates summary charts
- `clean_orders.csv`: Final cleaned dataset exported for Tableau

## 3. QA & Governance
- `pytest` tests: Validate quality rules
- `qa_summary.csv`: Summary table of pass/fail rules
- `steward_issues.csv`: Log of issues with status and severity
- `data_dictionary.csv`: Column-level metadata

## 4. Output
- Tableau Dashboard: Visualizes sales, QA, and governance KPIs

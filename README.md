# Credit-Risk-Dashboard


## 1. Overview
This project is a **Credit Risk Monitoring Dashboard** built using **Python** and **SQLite**.  
It analyzes credit card client data to generate key risk metrics such as average credit limits, default rates by demographics, monthly bill and payment trends, and payment delays vs default risk.

The project demonstrates **Python, Pandas, SQL, and data visualization** skills with an end-to-end analysis pipeline—from raw CSV data to clean insights and visual reports.

## 2. Dataset
Based on the UCI Credit Card Default Dataset with 30,000 clients.  
Columns include demographics, credit limits, bill/payment amounts, repayment history, and default status.

## 3. Technologies Used
- Python 3 (pandas, sqlite3, matplotlib, seaborn, openpyxl)
- SQLite database
- Excel export for processed data and query results

## 4. Project Workflow
- Load and clean CSV data (standardize column names)
- Calculate key metrics and group analyses in Python
- Store cleaned data in SQLite and run analytical SQL queries
- Visualize insights with charts
- Export cleaned data and SQL results to Excel files

## 5. SQL Skills Demonstrated
- Aggregations with `GROUP BY`
- Conditional grouping with `CASE`
- Multi-column averages

## 6. How to Run
1. Install required Python packages:  pip install pandas matplotlib seaborn openpyxl
2. Place `credit_data.csv` and `Dashboard.py` together.  
3. Run the script:  python Dashboard.py
4. Review terminal outputs and charts that pop up.  
5. Check generated Excel files for cleaned data and query results.

## 7. Benefits
- End-to-end data pipeline demonstration  
- Solid Python and SQL querying showcase  
- Clear visual and exportable reporting  

## 8. Future Extensions
- Add interactive UI (Streamlit/Dash)  
- Build ML model for default prediction  
- Schedule automated reports  


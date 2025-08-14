import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv("UCI_Credit_Card.csv")
print("Data Loaded:\n", df.head())

# 2. Basic info and cleaning
print("\nData Info:\n")
print(df.info())

# Make sure numeric columns are properly typed
numeric_cols = df.columns.drop(["ID"])
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

# 3. Summary metrics (Python side)
avg_limit = df["LIMIT_BAL"].mean()
default_rate = df["default payment next month"].mean() * 100
avg_age = df["AGE"].mean()

print(f"\nAverage Credit Limit: {avg_limit:,.2f}")
print(f"Default Rate: {default_rate:.2f}%")
print(f"Average Age: {avg_age:.1f} years")

# Default rates by education level
default_by_edu = df.groupby("EDUCATION")["default payment next month"].mean() * 100
print("\nDefault rate by education:\n", default_by_edu)

# 4. Store DataFrame into SQLite
conn = sqlite3.connect("credit_card.db")
df.to_sql("credit_clients", conn, if_exists="replace", index=False)

# 5. SQL QUERIES (examples)
print("\nRunning SQL queries...\n")

# Example 1: Average credit limit by marriage status
query1 = """
SELECT MARRIAGE, AVG(LIMIT_BAL) AS avg_limit
FROM credit_clients
GROUP BY MARRIAGE
ORDER BY avg_limit DESC;
"""
result1 = pd.read_sql_query(query1, conn)
print("Average Limit by Marriage Status:\n", result1)

# Example 2: Default rate by age group
query2 = """
SELECT 
    CASE
        WHEN AGE < 30 THEN 'Under 30'
        WHEN AGE BETWEEN 30 AND 50 THEN '30-50'
        ELSE '50+'
    END AS age_group,
    ROUND(AVG("default payment next month") * 100, 2) AS default_rate
FROM credit_clients
GROUP BY age_group;
"""
result2 = pd.read_sql_query(query2, conn)
print("\nDefault Rate by Age Group:\n", result2)

# Example 3: Monthly average bill amounts
query3 = """
SELECT 
    ROUND(AVG(BILL_AMT1), 2) AS avg_bill_m1,
    ROUND(AVG(BILL_AMT2), 2) AS avg_bill_m2,
    ROUND(AVG(BILL_AMT3), 2) AS avg_bill_m3
FROM credit_clients;
"""
result3 = pd.read_sql_query(query3, conn)
print("\nAverage Bill Amounts:\n", result3)

# 6. Visualizations
# Plot default rate by education level
plt.figure(figsize=(8,5))
sns.barplot(x=default_by_edu.index, y=default_by_edu.values, palette="viridis")
plt.title("Default Rate by Education Level")
plt.xlabel("Education Level")
plt.ylabel("Default Rate (%)")
plt.show()

# Age distribution
plt.figure(figsize=(8,5))
sns.histplot(df["AGE"], bins=10, kde=True)
plt.title("Age Distribution of Clients")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Payment delays vs Default
plt.figure(figsize=(8,5))
sns.boxplot(x="default payment next month", y="PAY_0", data=df)
plt.title("Payment Delay (Current Month) vs Default")
plt.xlabel("Default Next Month (0=No, 1=Yes)")
plt.ylabel("Delay in Months (PAY_0)")
plt.show()

df.to_excel("cleaned_credit_data.xlsx", index=False)

conn.close()

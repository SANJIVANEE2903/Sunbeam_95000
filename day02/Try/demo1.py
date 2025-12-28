import pandas as pd
import pandasql as ps

# Read CSV
sales_data = pd.read_csv("emp_hdr.csv")

# Check columns (optional)
print(sales_data.columns)
print(sales_data.head())

# SQL query using correct column names
query = """
SELECT ename,
       SUM(sal) AS total_salary,
       COUNT(*) AS cnt
FROM sales
GROUP BY ename
HAVING total_salary > 100
ORDER BY cnt DESC

"""

# Run query
result = ps.sqldf(query, {"sales": sales_data})
print(result)

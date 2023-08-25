"""
Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.
"""
import numpy as np
import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    x = np.sort(employee['salary'].unique())
    if N > x.size:
        return pd.DataFrame([])
    else:
        return pd.DataFrame([x[-N]])


"""
SQL Solution:
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set N = N-1;
  RETURN (
      select distinct(salary) from Employee
      order by salary desc
      limit 1 offset N
  );
END
"""

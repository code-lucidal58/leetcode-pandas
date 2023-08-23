"""
Table: Employees
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id is the primary key (column with unique values) for this table.
Each row of this table indicates the employee ID, employee name, and salary.

Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
"""
import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    x = (employees['employee_id']%2!=0) & (~employees['name'].str.startswith('M'))
    employees.loc[x,'bonus'] = employees['salary']
    return employees[['employee_id','bonus']].sort_values(by='employee_id')

"""
SQL Solution:
select employee_id,
case 
when employee_id%2=1 and name not like 'M%' then salary
else 0
end as bonus
from Employees
order by employee_id asc
"""

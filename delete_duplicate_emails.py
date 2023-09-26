"""
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
"""
import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id', inplace=True)
    person.drop_duplicates(subset=['email'], keep='first', inplace=True)


"""
SQL Solution:
DELETE n1 FROM Person n1, Person n2 WHERE n1.Id > n2.Id AND n1.Email = n2.Email
"""

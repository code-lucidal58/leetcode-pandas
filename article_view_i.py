"""
Table: Views
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date.
Note that equal author_id and viewer_id indicate the same person.

Write a solution to find all the authors that viewed at least one of their own articles.
"""
import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']][['author_id']]
    df.drop_duplicates(inplace=True)
    df.rename(columns={'author_id': 'id'}, inplace=True)
    df = df.sort_values(by=['id'])
    return df


"""
SQL Solution:
select distinct(author_id) as id
from Views
where author_id = viewer_id
order by id
"""

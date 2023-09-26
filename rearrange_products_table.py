"""
Table: Products
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
If the product is not available in a store, the price will be null in that store's column.

Write a solution to rearrange the Products table so that each row has (product_id, store, price).
If a product is not available in a store, do not include a row with that product_id and store combination
in the result table.
"""
import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # Simple solution
    df=pd.DataFrame(index=range(products.shape[0]*3), columns=['product_id','store','price'])
    s1 = products[['product_id','store1']].rename(columns={'store1':'price'}).dropna()
    s1['store'] = 'store1'
    s2 = products[['product_id','store2']].rename(columns={'store2':'price'}).dropna()
    s2['store'] = 'store2'
    s3 = products[['product_id','store3']].rename(columns={'store3':'price'}).dropna()
    s3['store'] = 'store3'
    df = pd.concat([s1,s2,s3],axis = 0, ignore_index=True)
    return df
    # Smart solution
    


"""
SQL Solution:
DELETE n1 FROM Person n1, Person n2 WHERE n1.Id > n2.Id AND n1.Email = n2.Email
"""

import pandas as pd

data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

"""
Write a solution to find all customers who never order anything.

Return the result table in any order.

The result format is in the following example.
Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
"""


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # returns "name" column from customers where customers["id"] not in orders["customerId"]
    a = customers[~customers["id"].isin(orders["customerId"])]["name"]
    # converts the series to df
    a = pd.DataFrame(a)
    # rename the column
    a = a.rename(columns={"name": "customers"})
    return a

find_customers(customers,orders)



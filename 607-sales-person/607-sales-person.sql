# Write your MySQL query statement below
# Sub quesry 2603 ms
# SELECT name 
# FROM SalesPerson
# WHERE sales_id NOT IN (
#     SELECT sales_id 
#     FROM Orders
#     WHERE com_id = (
#         SELECT com_id 
#         FROM Company
#         WHERE name = 'RED'
#     )
# )


# Join 993 ms
SELECT name
FROM SalesPerson
WHERE name NOT IN
    ( 
        SELECT s.name 
        FROM SalesPerson s
        JOIN Company c
        JOIN Orders o
        ON s.sales_id = o.sales_id AND c.com_id = o.com_id
        WHERE c.name = 'RED'
    )



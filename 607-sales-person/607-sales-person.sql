# Write your MySQL query statement below
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

select SalesPerson.name
from SalesPerson
where SalesPerson.name not in
( select salesperson.name from
SalesPerson join Company join Orders
ON SalesPerson.sales_id = Orders.sales_id and Company.com_id = Orders.com_id
where Company.name = 'RED')



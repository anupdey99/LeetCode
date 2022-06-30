# Write your MySQL query statement below
SELECT 
    u.user_id AS buyer_id, 
    u.join_date, 
    COUNT(order_id) AS orders_in_2019
FROM Users u 
LEFT JOIN
    (
        SELECT order_id, buyer_id
        FROM Orders
        WHERE YEAR(order_date) = '2019'
    ) AS o
ON o.buyer_id = u.user_id
GROUP BY u.user_id


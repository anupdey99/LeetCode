# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE a
FROM Person a, Person b
WHERE a.id > b.id AND a.email = b.email
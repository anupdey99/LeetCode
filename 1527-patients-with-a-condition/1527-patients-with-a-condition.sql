# Write your MySQL query statement below
SELECT *
FROM Patients
WHERE 
    conditions LIKE 'DIAB1%' #if appear in first
    OR
    conditions LIKE '% DIAB1%' #if appear in elsewhere
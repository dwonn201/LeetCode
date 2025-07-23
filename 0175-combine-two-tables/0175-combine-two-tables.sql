# Write your MySQL query statement below
select 
    A.firstName,
    A.lastName,
    B.city,
    B.state
from Person as A
left join Address as B on A.personId = B.personId
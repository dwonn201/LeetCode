# Write your MySQL query statement below
select  A.id, coalesce(B.student, A.student) as student
from Seat as A 
left join Seat as B 
on (
        (A.id % 2 = 1 and B.id = A.id +1) or 
        (A.id % 2 = 0 and B.id = A.id -1) 
    )
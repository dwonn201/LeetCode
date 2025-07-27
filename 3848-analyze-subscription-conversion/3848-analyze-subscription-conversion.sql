# Write your MySQL query statement below
with step1 as (
    select 
        user_id,
        round(avg(case when activity_type = 'free_trial' then activity_duration else null end),2) as trial_avg_duration,
        round(avg(case when activity_type = 'paid' then activity_duration else null end),2) as paid_avg_duration
    from UserActivity
    group by 1
)
select *
from step1 
where paid_avg_duration is not null
order by 1
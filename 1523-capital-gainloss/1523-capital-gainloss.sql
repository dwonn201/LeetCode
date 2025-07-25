# Write your MySQL query statement below
with step1 as (
    select 
        stock_name,
        case 
            when operation = 'Buy' then -1 * price
            else price
        end as operation_price
    from Stocks 
)
select 
    stock_name, 
    sum(operation_price) as capital_gain_loss
from step1
group by 1 
order by 1 
;
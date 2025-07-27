# Write your MySQL query statement below
select 
    sample_id, 
    dna_sequence,
    species,
    case when substring(dna_sequence, 1,3) = 'ATG' then 1 else 0 end as has_start,
    case when right(dna_sequence, 3) in ('TAA', 'TAG', 'TGA') then 1 else 0 end as has_stop,
    case when dna_sequence like '%ATAT%' then 1 else 0 end as has_atat,
    case when dna_sequence like '%GGG%' then 1 else 0 end as has_ggg
from Samples
order by 1,2,3
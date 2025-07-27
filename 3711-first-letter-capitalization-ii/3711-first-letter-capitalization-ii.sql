# Write your MySQL query statement below
with recursive TitleCaseConverter as (
    -- 1. 재귀의 시작점(Anchor)을 정의합니다.
    -- 각 문자열의 첫 글자를 대문자로 변환하고, 처리할 위치를 2로 설정합니다.
    select 
        content_id,
        content_text as original_text,
        cast(upper(substring(content_text, 1, 1)) as char(1000)) as converted_text,
        2 as position
    from user_content

    union all 
    -- 2. 재귀 부분(Recursive Member)을 정의합니다.
    -- 문자열의 끝에 도달할 때까지 한 글자씩 처리합니다.
    select
        content_id,
        original_text,
        concat(
            converted_text,
            case
                when substring(original_text, position-1,1) in (' ','-')
                then upper(substring(original_text, position, 1))
                else lower(substring(original_text, position, 1))
            end
        ),
        position + 1
    from TitleCaseConverter
    where 1=1 
    -- 처리할 위치(position)가 문자열의 길이보다 작거나 같을 때까지 반복합니다.
    and position <= LENGTH(original_text)
),
final as (
    select 
        content_id,
        original_text,
        converted_text,
        -- 각 content_id 별로 position이 가장 큰, 즉 마지막 변환 결과에 1번을 매깁니다.
        row_number() over (partition by content_id order by position desc) as rn
    from TitleCaseConverter
)
select
    content_id, 
    original_text,
    converted_text
from final
where rn = 1
order by content_id
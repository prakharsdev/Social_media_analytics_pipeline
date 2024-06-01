with twitter_data as (
    select
        id,
        created_at,
        text
    from
        {{ ref('twitter_data') }}
)

select
    id,
    created_at,
    text,
    length(text) as text_length,
    case
        when lower(text) like '%#datapipeline%' then 1
        else 0
    end as is_datapipeline_related
from
    twitter_data

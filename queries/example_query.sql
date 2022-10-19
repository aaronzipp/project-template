select
    id,
    url,
    creation_date,
    description,
    visits
from database.schema.table
where creation_date >= to_date('2022-01-01', 'YYYY-MM-DD')
    and
    visits >= 1000
    and description is not null;

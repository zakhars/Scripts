-- Select every 10-th record from table

select t.RiskTime, t.TimeReceived
from
(
    select RiskTime, TimeReceived, row_number() over (order by TimeReceived) as RowNum
    from RSRequests
    where RequestType = 'OrderRequest'
) as t
where t.RowNum % 10 = 0
order by t.TimeReceived

-- explain (analyze, buffers) 
-- "2022-05-11 17:00:00.014783"	"2022-05-12 16:08:53.742941"

SELECT DISTINCT ON (type_uuid) *
FROM public.log_1
INNER JOIN log_types on log_1.type_uuid = log_types.uuid
WHERE

-- 	log_1.created_at < CURRENT_TIMESTAMP + '0 DAY'::interval
-- and log_1.created_at > CURRENT_TIMESTAMP - '1 DAY'::interval

	log_1.created_at < CURRENT_TIMESTAMP + ((RANDOM()+0.01)::float*23 || ' HOURS')::interval
AND log_1.created_at > CURRENT_TIMESTAMP - ((RANDOM()+0.01)::float*23 || ' HOURS')::interval

ORDER BY type_uuid, log_1.created_at desc
-- group by  type_uuid

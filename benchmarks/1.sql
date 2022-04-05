-- explain (analyze, buffers) 
SELECT DISTINCT ON (type_uuid) * FROM public.log_1
-- SELECT count(*), type_uuid FROM public.log_1
inner join log_types on log_1.type_uuid = log_types.uuid
where 
--	log_1.created_at < CURRENT_TIMESTAMP + '0 DAY'::interval
-- and 
log_1.created_at > CURRENT_TIMESTAMP - '1 DAY'::interval
order by type_uuid, log_1.created_at desc
-- group by  type_uuid

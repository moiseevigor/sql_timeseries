-- SELECT
--     pg_size_pretty (pg_indexes_size('idx_tis_config_uuid_image_occlusion_type_created_datetime'));     
--	 pg_size_pretty (pg_tablespace_size('pg_default'));

/*	 
SELECT
	pg_database.datname,
	pg_size_pretty(pg_database_size(pg_database.datname)) AS size
FROM pg_database;
*/
/*
SELECT
    relname AS "relation",
    pg_size_pretty (
        pg_total_relation_size (C .oid)
    ) AS "total_size"
FROM
    pg_class C
LEFT JOIN pg_namespace N ON (N.oid = C .relnamespace)
WHERE
    nspname NOT IN (
        'pg_catalog',
        'information_schema'
    )
AND C .relkind <> 'i'
AND nspname !~ '^pg_toast'
ORDER BY
    pg_total_relation_size (C .oid) DESC
LIMIT 10;
*/


-- SELECT pg_size_pretty (pg_total_relation_size ('log_1'));

-- SELECT pg_size_pretty (pg_total_relation_size('log_1'));
-- select '2022-04-05 13:59:55.568134+00'::timestamp, '2022-04-05 13:59:55.568134+00'::timestamp + '0.5 SECOND'::interval

-- SELECT count(*) FROM public.log_1
-- SELECT pg_size_pretty (pg_total_relation_size('idx_type_uuid_created_at'));
-- SELECT pg_size_pretty (pg_total_relation_size('log_1'));
SELECT pg_size_pretty (pg_total_relation_size('idx_created_at'));



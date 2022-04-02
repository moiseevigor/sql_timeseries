
-- Table: public.log_1

DROP TABLE IF EXISTS public.log_1;

CREATE TABLE IF NOT EXISTS public.log_1
(
    uuid uuid NOT NULL,
    created_at timestamp without time zone,
    text character varying COLLATE pg_catalog."default",
    CONSTRAINT log_1_pkey PRIMARY KEY (uuid)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.log_1
    OWNER to tsuser;

-- Index: idx_created_at

DROP INDEX IF EXISTS public.idx_created_at;

CREATE INDEX IF NOT EXISTS idx_created_at
    ON public.log_1 USING btree
    (created_at DESC NULLS FIRST)
    TABLESPACE pg_default;


-- Table: public.log_1

DROP TABLE IF EXISTS public.log_1;

CREATE TABLE IF NOT EXISTS public.log_1
(
    uuid uuid NOT NULL,
    type_uuid uuid NOT NULL,
    created_at timestamp without time zone,
    text character varying COLLATE pg_catalog."default",
    CONSTRAINT log_1_pkey PRIMARY KEY (uuid)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.log_1
    OWNER to tsuser;

-- Table: public.log_types

DROP TABLE IF EXISTS public.log_types;

CREATE TABLE IF NOT EXISTS public.log_types
(
    uuid uuid NOT NULL,
    created_at timestamp without time zone,
    text character varying COLLATE pg_catalog."default",
    CONSTRAINT log_types_pkey PRIMARY KEY (uuid)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.log_types
    OWNER to tsuser;

-- Table: public.experiments

DROP TABLE IF EXISTS public.experiments;

CREATE TABLE IF NOT EXISTS public.experiments
(
    id INT NOT NULL,
    created_at timestamp without time zone,
    text character varying COLLATE pg_catalog."default",
    CONSTRAINT experiments_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.experiments
    OWNER to tsuser;

-- Table: public.experiment_results

DROP TABLE IF EXISTS public.experiment_results;

CREATE TABLE IF NOT EXISTS public.experiment_results
(
    id INT NOT NULL,
    experiment_id INT NOT NULL,
    created_at timestamp without time zone,
    text character varying COLLATE pg_catalog."default",
    CONSTRAINT experiment_results_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.experiments
    OWNER to tsuser;


-- Index: idx_created_at

DROP INDEX IF EXISTS public.idx_created_at;

CREATE INDEX IF NOT EXISTS idx_created_at
    ON public.log_1 USING btree
    (created_at DESC NULLS FIRST)
    TABLESPACE pg_default;

-- Index: idx_type_uuid_created_at

-- DROP INDEX IF EXISTS public.idx_type_uuid_created_at;

CREATE INDEX IF NOT EXISTS idx_type_uuid_created_at
    ON public.log_1 USING btree
    (type_uuid ASC NULLS LAST, created_at DESC NULLS FIRST)
    TABLESPACE pg_default;

-- Constraint: fk_type_uuid

ALTER TABLE IF EXISTS public.log_1 DROP CONSTRAINT IF EXISTS fk_type_uuid;

ALTER TABLE IF EXISTS public.log_1
    ADD CONSTRAINT fk_type_uuid FOREIGN KEY (type_uuid)
    REFERENCES public.log_types (uuid) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE RESTRICT
    NOT VALID;

-- populate log_types

/*
INSERT INTO public.log_types VALUES
    ('7a4721b0-b4d3-11ec-a28a-0242ac110002', CURRENT_TIMESTAMP, 'type 1'),
    ('9140eca2-b4d3-11ec-a28a-0242ac110002', CURRENT_TIMESTAMP, 'type 2'),
    ('97957e9c-b4d3-11ec-a28a-0242ac110002', CURRENT_TIMESTAMP, 'type 3'),
    ('9d7014e4-b4d3-11ec-a28a-0242ac110002', CURRENT_TIMESTAMP, 'type 4');
*/
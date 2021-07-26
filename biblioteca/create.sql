create database biblioteca;

CREATE TABLE lector
(
    id_lector integer NOT NULL DEFAULT nextval('lector_id_lector_seq'::regclass),
    codigo_lector character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nombres character varying(50) COLLATE pg_catalog."default" NOT NULL,
    apellido_paterno character varying(50) COLLATE pg_catalog."default" NOT NULL,
    apellido_materno character varying(50) COLLATE pg_catalog."default" NOT NULL,
    dni character varying(8) COLLATE pg_catalog."default" NOT NULL,
    edad integer NOT NULL,
    telefono character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT pk_lector PRIMARY KEY (id_lector)
);

CREATE TABLE libros
(
    id_libro integer NOT NULL DEFAULT nextval('libros_id_libro_seq'::regclass),
    codigo_libro character varying(10) COLLATE pg_catalog."default" NOT NULL,
    titulo character varying(30) COLLATE pg_catalog."default" NOT NULL,
    autor character varying(30) COLLATE pg_catalog."default" NOT NULL,
    categoria character varying(30) COLLATE pg_catalog."default" NOT NULL,
    paginas integer NOT NULL,
    editorial character varying(30) COLLATE pg_catalog."default" NOT NULL,
    condicion character varying(10) COLLATE pg_catalog."default" NOT NULL,
    descripcion character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT pk_libros PRIMARY KEY (id_libro)
);

CREATE TABLE prestamos
(
    id_prestamo integer NOT NULL DEFAULT nextval('prestamos_id_prestamo_seq'::regclass),
    id_lector integer NOT NULL,
    id_libro integer NOT NULL,
    alquilado timestamp without time zone,
    devuelto timestamp without time zone,
    CONSTRAINT fk_prestamos_lector FOREIGN KEY (id_lector)
        REFERENCES public.lector (id_lector) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_prestamos_libro FOREIGN KEY (id_libro)
        REFERENCES public.libros (id_libro) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
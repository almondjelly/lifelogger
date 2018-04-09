--
-- PostgreSQL database dump
--

-- Dumped from database version 10.3
-- Dumped by pg_dump version 10.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: weeklyreview; Type: TABLE; Schema: public; Owner: gail
--

CREATE TABLE public.weeklyreview (
    id integer NOT NULL,
    week_start date,
    week_end date,
    question text
);


ALTER TABLE public.weeklyreview OWNER TO gail;

--
-- Name: weeklyreview_id_seq; Type: SEQUENCE; Schema: public; Owner: gail
--

CREATE SEQUENCE public.weeklyreview_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.weeklyreview_id_seq OWNER TO gail;

--
-- Name: weeklyreview_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: gail
--

ALTER SEQUENCE public.weeklyreview_id_seq OWNED BY public.weeklyreview.id;


--
-- Name: weeklyreview id; Type: DEFAULT; Schema: public; Owner: gail
--

ALTER TABLE ONLY public.weeklyreview ALTER COLUMN id SET DEFAULT nextval('public.weeklyreview_id_seq'::regclass);


--
-- Data for Name: weeklyreview; Type: TABLE DATA; Schema: public; Owner: gail
--

COPY public.weeklyreview (id, week_start, week_end, question) FROM stdin;
\.


--
-- Name: weeklyreview_id_seq; Type: SEQUENCE SET; Schema: public; Owner: gail
--

SELECT pg_catalog.setval('public.weeklyreview_id_seq', 1, false);


--
-- Name: weeklyreview weeklyreview_pkey; Type: CONSTRAINT; Schema: public; Owner: gail
--

ALTER TABLE ONLY public.weeklyreview
    ADD CONSTRAINT weeklyreview_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--


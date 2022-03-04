--DROP DATABASE
drop database polyservicedb;

--CREATE DATABASE
create database polyservicedb;

-- SET OWNER
alter database polyservicedb owner to polyserviceuser;

-- ENABLE POSTIGS EXTENSION
\c polyservicedb
CREATE EXTENSION postgis;


drop database polyservicedb; create database polyservicedb; alter database polyservicedb owner to polyserviceuser;
\c polyservicedb
CREATE EXTENSION postgis;

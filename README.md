# PolyService API

## DESCRIPCIÓN:

API to allow transportation suppliers to add their service areas as polygons. 

[On github](https://github.com/0xalen/polyservice "PolyService API")

## DEPENDENCIES
(In Fedora)
- PostgreSLQ: postgresql-server 
- PostGIS: postgis
- Python: python3 python3-venv

NOTE: After installing postgis it should be enabled on the database running:
```
~# su postgres
~$ psql 
postgres=# \c polyservicedb 
postgres=# CREATE EXTENSION postgis;
CREATE EXTENSION
```

 

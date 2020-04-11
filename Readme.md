## Project Startup

Run
```
$ docker-compose up -d
$ docker exec -it omni_seeker /bin/bash
```

## DATABASE

Create database running the following command
```
$ docker exec -ti omni_seeker  sh -c 'createdb -U postgres --lc-collate=C --lc-ctype=C -E LATIN1 -T template0 predicao_for_db'
```
## FIX USER OWNERSHIP
```
$ chown -R 1000:1000 ./migrations
```
## YOYO MIGRATIONS
Examples:
```
$ yoyo new ./migrations -m "create table table_name"
$ yoyo new ./migrations -m "add column column_name"

```

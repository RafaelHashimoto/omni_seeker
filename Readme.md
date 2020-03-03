docker-compose up -d
docker exec -it omni_seeker /bin/bash


Criando migration
yoyo new ./migrations -m "nome da migration"

Aplicando migration
yoyo apply
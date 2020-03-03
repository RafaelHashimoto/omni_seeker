"""
create municipios
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        "create table municipios ("
            "id SERIAL PRIMARY KEY,"
            "codigo varchar(10),"
            "nome varchar(100),"
            "codigo_unidade_federacao integer,"
            "geoibge_id varchar(30)"
        ")"
    )
]

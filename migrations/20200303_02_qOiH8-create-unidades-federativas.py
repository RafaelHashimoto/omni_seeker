"""
create unidades federativas
"""

from yoyo import step

__depends__ = {'20200303_01_ZOgen-create-municipios'}

steps = [
    step(
        "create table unidades_federacao ("
	        "id SERIAL PRIMARY KEY,"
	        "codigo integer,"
	        "sigla varchar(10),"
	        "nome varchar(100)"
        ")"
    )
]

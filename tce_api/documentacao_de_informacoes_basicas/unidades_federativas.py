import requests
import psycopg2
import pdb

try:
    db_connection = psycopg2.connect(
        host='db', database='omni_seeker_db',
        user='postgres', password='root'
    )

    cursor = db_connection.cursor()

    response = requests.get('https://api.tce.ce.gov.br/index.php/sim/1_0/unidades_federacao.json')

    for params in response.json()['rsp']['_content']:
        cursor.execute(
            'INSERT INTO unidades_federacao (codigo, sigla, nome) VALUES(%s, %s, %s)',
            (params['codigo_unidade_federacao'], params['sigla_unidade_federacao'], params['nome_unidade_federacao'])
        )
    db_connection.commit()
    cursor.close()
except psycopg2.DatabaseError as error:
    print(error)
import requests
import psycopg2
import pdb

try:
    db_connection = psycopg2.connect(
        host='db', database='omni_seeker_db',
        user='postgres', password='root'
    )

    cursor = db_connection.cursor()

    response = requests.get('https://api.tce.ce.gov.br/index.php/sim/1_0/municipios.json')

    for params in response.json()['rsp']['_content']:
        cursor.execute(
            'INSERT INTO municipios (codigo, nome, geoibge_id, codigo_unidade_federacao )VALUES(%s, %s, %s, %s)',
            (params['codigo_municipio'], params['nome_municipio'], params['geoibgeId'], params['geoibgeId'][:2])
        )
    db_connection.commit()
    cursor.close()
except psycopg2.DatabaseError as error:
    print(error)
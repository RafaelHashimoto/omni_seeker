from tce_api.base import Base
import pdb
import psycopg2
class Municipios(Base):
    def __init__(self):
        super().__init__()
        self.cursor = self.db_connection.cursor()
        self.base_method = 'municipios.json'

    def execute(self):
        try:
            response = self.requests.get(self.base_url+self.base_method)
            for params in response.json()['rsp']['_content']:
                self.cursor.execute(
                    'INSERT INTO municipios (codigo, nome, geoibge_id, codigo_unidade_federacao )VALUES(%s, %s, %s, %s)',
                    (params['codigo_municipio'], params['nome_municipio'], params['geoibgeId'], params['geoibgeId'][:2])
                )
            self.db_connection.commit()
            self.cursor.close()
        except psycopg2.DatabaseError as error:
            print(error)

from tce_api.base import Base
import pdb
import psycopg2
class UnidadesFederativas(Base):
    def __init__(self):
        super().__init__()
        self.cursor = self.db_connection.cursor()
        self.base_method = 'unidades_federacao.json'

    def execute(self):
        try:
            response = self.requests.get(self.base_url+self.base_method)
            for params in response.json()['rsp']['_content']:
                self.cursor.execute(
                    'INSERT INTO unidades_federativas (codigo, sigla, nome) VALUES(%s, %s, %s)',
                    (params['codigo_unidade_federacao'], params['sigla_unidade_federacao'], params['nome_unidade_federacao'])
                )
            self.db_connection.commit()
            self.cursor.close()
        except psycopg2.DatabaseError as error:
            print(error)
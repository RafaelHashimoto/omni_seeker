from tce_api.base import Base
from itertools import repeat
from datetime import datetime

import pdb
import psycopg2

class Orgaos(Base):
    def __init__(self):
        super().__init__()
        self.municipios = self.get_municipios()
        self.cursor = self.db_connection.cursor()
        self.base_method = 'orgaos.json'
        self.year = 2015

    def execute(self):
        try:
            for municipio in self.municipios:
                for year in repeat(self.year, datetime.now().year):
                    response = self.requests.get(self.url_with_params(municipio[0], year))
                    for params in response.json()['rsp']['_content']:
                        self.cursor.execute(
                            "INSERT INTO orgaos"
                                "("
                                      "codigo_municipio, exercicio_orcamento,"
                                      "codigo_orgao, codigo_tipo_unidade,"
                                      "nome_orgao, cgc_orgao"
                                ")"
                            "VALUES(%s, %s, %s, %s, %s, %s)",
                            (
                                params['codigo_municipio'], params['exercicio_orcamento'],
                                params['codigo_orgao'], params['codigo_tipo_unidade'],
                                params['nome_orgao'], params['cgc_orgao']
                            )
                        )
                    self.db_connection.commit()
                    self.cursor.close()
        except psycopg2.DatabaseError as error:
            print(error)

    def url_with_params(self, city, year):
        return (  self.base_url + self.base_method +
                  '?codigo_municipio=' + city +
                  '&exercicio_orcamento=' + str(year) )

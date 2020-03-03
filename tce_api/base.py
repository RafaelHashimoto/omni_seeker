import requests
import psycopg2
import pdb

class Base:
    def __init__(self):
        self.db_connection = self.database_connection()
        self.base_url = 'https://api.tce.ce.gov.br/index.php/sim/1_0/'
        self.requests = requests

    def database_connection(self):
        return psycopg2.connect(host='db', database='omni_seeker_db', user='postgres', password='root')

    def get_municipios(self):
      db_connection = self.database_connection()
      cursor = db_connection.cursor()
      cursor.execute('select codigo from municipios')
      municipios = cursor.fetchall()
      cursor.close()
      return municipios
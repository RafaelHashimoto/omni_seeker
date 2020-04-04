import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:root@db/omni_seeker_db')
session = sessionmaker(bind=engine)

class Base:
    def __init__(self):
        self.base_url = 'https://api.tce.ce.gov.br/index.php/sim/1_0/'

    def request_tce_api(self, method, params):
        return requests.get(self.base_url + method + params)

    def get_municipios(self):
      db_connection = self.database_connection()
      cursor = db_connection.cursor()
      cursor.execute('select codigo from municipios')
      municipios = cursor.fetchall()
      cursor.close()
      return municipios

    def get_tce_request_monitor(self, method):
        db_connection = self.database_connection()
        cursor = db_connection.cursor()
        cursor.execute("select id from tce_request_monitor where method = '%s'" %(method))
        monitor = cursor.fetchall()
        cursor.close()
        return monitor

    def save_progress(self, method, year, error, success):
        tce_request_monitor = self.get_tce_request_monitor(method)
        cursor = self.get_db_cursor()
        cursor.execute(
            "INSERT INTO tce_request_monitor (method, year, error, success)"
            "VALUES(%s, %s, %s, %s)",
            (method, year, error.__doc__, success)
        )
        self.db_connection.commit()
        cursor.close()
from tce_api.base import Base
import pdb
import psycopg2
from model.municipio import Municipio
class Municipios(Base):
    def __init__(self):
        super().__init__()
        self.base_method = 'municipios.json'

    def execute(self):
        response = self.request_tce_api(self.base_method, '')
        municipios = []
        for params in response.json()['rsp']['_content']:
            municipios.append(Municipio(params))
        Municipio.save_multiple(municipios)
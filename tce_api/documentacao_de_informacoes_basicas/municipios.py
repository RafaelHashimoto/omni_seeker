from tce_api.base import Base
from models.municipio import Municipio
class Municipios(Base):
    def __init__(self):
        super().__init__()
        self.initialize_variables_by_method('municipios')

    def execute(self):
        try:
            if self.requestable():
                response = self.request_tce_api()
                municipios = []
                for params in response.json()['rsp']['_content']:
                    municipios.append(Municipio(params))
                Municipio.save_multiple(municipios)
                self.save_progress('', True)
        except Exception as e:
            self.save_progress(e, False)
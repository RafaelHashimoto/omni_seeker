from tce_api.base import Base
from datetime import datetime
from models.municipio import Municipio

class ByCityRequester(Base):
    def __init__(self, method, cls):
        super().__init__()
        self.initialize_variables_by_method(cls.__table__.name)
        self.cls = cls

    def execute(self):
        try:
            for municipio in Municipio.by_id_range(self.municipio_id):
                self.municipio_id = municipio.id
                array = []
                for year in range(self.year, datetime.now().year):
                    self.year = year
                    response = self.request_tce_api(self.url_with_params(municipio.codigo))
                    for params in response['rsp']['_content']:
                        array.append(self.cls(params))
                self.cls.save_multiple(array)
            self.save_progress('', True)
        except Exception as e:
            self.save_progress(e, False)

    def url_with_params(self, codigo):
        return ('?codigo_municipio=' + codigo + '&exercicio_orcamento=' + str(self.year))
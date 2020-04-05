from tce_api.base import Base
from models.unidade_federativa import UnidadeFederativa
import pdb
class UnidadesFederativas(Base):
    def __init__(self):
        super().__init__()
        self.initialize_variables_by_method('unidades_federacao')

    def execute(self):
        try:
            if self.requestable():
                unidades_federativas = []
                response = self.request_tce_api()
                for params in response.json()['rsp']['_content']:
                    unidades_federativas.append(UnidadeFederativa(params))
                UnidadeFederativa.save_multiple(unidades_federativas)
                self.save_progress('', True)
        except Exception as e:
            self.save_progress(e, False)

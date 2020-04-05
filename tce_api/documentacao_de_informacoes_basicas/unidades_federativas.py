from tce_api.base import Base
from model.unidade_federativa import UnidadeFederativa

class UnidadesFederativas(Base):
    def __init__(self):
        super().__init__()
        self.initialize_variables_by_method('unidades_federacao')

    def execute(self):
        try:
            response = self.request_tce_api(self.method + '.json', '')
            unidades_federativas = []
            for params in response.json()['rsp']['_content']:
                unidades_federativas.append(UnidadeFederativa(params))
            UnidadeFederativa.save_multiple(unidades_federativas)
            self.save_progress('', True)
        except Exception as e:
            self.save_progress(e, False)

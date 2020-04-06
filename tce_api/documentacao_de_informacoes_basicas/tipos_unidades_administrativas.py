from tce_api.base import Base
from models.tipo_unidade_administrativa import TipoUnidadeAdministrativa

class TiposUnidadesAdministrativas(Base):
    def __init__(self):
        super().__init__()
        self.initialize_variables_by_method('tipos_unidades_administrativas')

    def execute(self):
        try:
            if self.requestable():
                response = self.request_tce_api()
                tipos_unidades_administrativas = []
                for params in response.json()['rsp']['_content']:
                    tipos_unidades_administrativas.append(TipoUnidadeAdministrativa(params))
                TipoUnidadeAdministrativa.save_multiple(tipos_unidades_administrativas)
                self.save_progress('', True)
        except Exception as e:
            self.save_progress(e, False)
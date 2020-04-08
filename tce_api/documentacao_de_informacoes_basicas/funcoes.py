from tce_api.base import Base
from models.funcao import Funcao
class Funcoes(Base):
    def __init__(self):
        super().__init__()
        self.initialize_variables_by_method('funcoes')

    def execute(self):
        try:
            if self.requestable():
                response = self.request_tce_api()
                funcoes = []
                for params in response.json()['rsp']['_content']:
                    funcoes.append(Funcao(params))
                Funcao.save_multiple(funcoes)
                self.save_progress('', True)
        except Exception as e:
            self.save_progress(e, False)
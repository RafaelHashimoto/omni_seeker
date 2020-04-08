from sqlalchemy import Column, Integer, String, DateTime
from models.base import Base

class Ordenador(Base):
	__tablename__ = 'ordenadores'

	id = Column(Integer, primary_key=True)
	codigo_municipio = Column(String)
	exercicio_orcamento = Column(String)
	codigo_unidade_gestora = Column(String)
	codigo_orgao = Column(String)
	codigo_unidade = Column(String)
	data_inclusao_unidade_orcamentaria = Column(DateTime)
	cpf_servidor = Column(String)
	codigo_ingresso = Column(String)
	codigo_vinculo = Column(String)
	numero_expediente_nomeacao = Column(String)
	data_inicio_gestao_ordenador = Column(DateTime)
	data_referencia_ordenador = Column(String)
	nome_ordenador = Column(String)
	data_fim_gestao_ordenador = Column(DateTime)
	tipo_cargo = Column(String)

	def __init__(self, params):
		self.codigo_municipio = params['codigo_municipio']
		self.exercicio_orcamento = params['exercicio_orcamento']
		self.codigo_unidade_gestora = params['codigo_unidade_gestora']
		self.codigo_orgao = params['codigo_orgao']
		self.codigo_unidade = params['codigo_unidade']
		self.data_inclusao_unidade_orcamentaria = params['data_inclusao_unidade_orcamentaria'] if params['data_inclusao_unidade_orcamentaria'] != '' else None
		self.cpf_servidor = params['cpf_servidor']
		self.codigo_ingresso = params['codigo_ingresso']
		self.codigo_vinculo = params['codigo_vinculo']
		self.numero_expediente_nomeacao = params['numero_expediente_nomeacao']
		self.data_inicio_gestao_ordenador = params['data_inicio_gestao_ordenador'] if params['data_inicio_gestao_ordenador'] != '' else None
		self.data_referencia_ordenador = params['data_referencia_ordenador']
		self.nome_ordenador = params['nome_ordenador']
		self.data_fim_gestao_ordenador = params['data_fim_gestao_ordenador']  if params['data_fim_gestao_ordenador'] != '' else None
		self.tipo_cargo = params['tipo_cargo']

	@classmethod
	def save_multiple(cls, array):
		cls.session.add_all(array)
		cls.session.commit()

	@classmethod
	def all(cls):
		return cls.session.query(cls).all()






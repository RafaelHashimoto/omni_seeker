from sqlalchemy import Column, Integer, String
from models.base import Base

class UnidadeOrcamentaria(Base):
	__tablename__ = 'unidades_orcamentarias'

	id = Column(Integer, primary_key=True)
	codigo_municipio = Column(String)
	exercicio_orcamento = Column(String)
	codigo_orgao = Column(String)
	codigo_unidade = Column(String)
	codigo_tipo_unidade = Column(String)
	nome_unidade = Column(String)
	tipo_administracao_unidade = Column(String)

	def __init__(self, params):
		self.codigo_municipio = params['codigo_municipio']
		self.exercicio_orcamento = params['exercicio_orcamento']
		self.codigo_orgao = params['codigo_orgao']
		self.codigo_unidade = params['codigo_unidade']
		self.codigo_tipo_unidade = params['codigo_tipo_unidade']
		self.nome_unidade = params['nome_unidade']
		self.tipo_administracao_unidade = params['tipo_administracao_unidade']

	@classmethod
	def save_multiple(cls, array):
		cls.session.add_all(array)
		cls.session.commit()

	@classmethod
	def all(cls):
		return cls.session.query(cls).all()

from sqlalchemy import Column, Integer, String
from model.base import Base

class Orgao(Base):
	__tablename__ = 'orgaos'

	id = Column(Integer, primary_key=True)
	codigo_municipio = Column(String)
	exercicio_orcamento = Column(String)
	codigo_orgao = Column(String)
	codigo_tipo_unidade = Column(String)
	nome_orgao = Column(String)
	cgc_orgao = Column(String)

	def __init__(self, params):
		self.codigo_municipio = params['codigo_municipio']
		self.exercicio_orcamento = params['exercicio_orcamento']
		self.codigo_orgao = params['codigo_orgao']
		self.codigo_tipo_unidade = params['codigo_tipo_unidade']
		self.nome_orgao = params['nome_orgao']
		self.cgc_orgao = params['cgc_orgao']

	@classmethod
	def save_multiple(cls, array):
		cls.session.add_all(array)
		cls.session.commit()

	@classmethod
	def all(cls):
		return cls.session.query(cls).all()
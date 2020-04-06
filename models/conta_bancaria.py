from models.base import Base
from sqlalchemy import Column, Integer, String, Text, Float

class ContaBancaria(Base):
	__tablename__ = 'contas_bancarias'

	id = Column(Integer, primary_key=True)
	codigo_municipio = Column(String)
	exercicio_orcamento = Column(String)
	codigo_orgao = Column(String)
	codigo_unidade = Column(String)
	numero_banco = Column(String)
	numero_agencia = Column(String)
	numero_conta = Column(String)
	data_abertura = Column(String)
	valor_saldo_abertura = Column(Float)
	data_referencia = Column(String)
	tipo_conta = Column(String)
	codigo_funcao = Column(String)
	descricao_objetivo = Column(Text)

	def __init__(self, params):
		self.codigo_municipio = params['codigo_municipio']
		self.exercicio_orcamento = params['exercicio_orcamento']
		self.codigo_orgao = params['codigo_orgao']
		self.codigo_unidade = params['codigo_unidade']
		self.numero_banco = params['numero_banco']
		self.numero_agencia = params['numero_agencia']
		self.numero_conta = params['numero_conta']
		self.data_abertura = params['data_abertura']
		self.valor_saldo_abertura = params['valor_saldo_abertura']
		self.data_referencia = params['data_referencia']
		self.tipo_conta = params['tipo_conta']
		self.codigo_funcao = params['codigo_funcao']
		self.descricao_objetivo = params['descricao_objetivo']

	@classmethod
	def all(cls):
		return cls.session.query(cls).all()

	@classmethod
	def save_multiple(cls, array):
		cls.session.add_all(array)
		cls.session.commit()
from sqlalchemy import Column, Integer, String, Float
from models.base import Base

class ContaExtraOrcamentaria(Base):
	__tablename__ = 'contas_extra_orcamentarias'

	id = Column(Integer, primary_key=True)
	codigo_municipio = Column(String)
	exercicio_orcamento = Column(String)
	codigo_conta_extra_orc = Column(String)
	desc_conta_extra_orc = Column(String)
	data_referencia_doc = Column(String)
	vl_saldo_ini = Column(Float)

	def __init__(self, params):
		self.codigo_municipio = params['codigo_municipio']
		self.exercicio_orcamento = params['exercicio_orcamento']
		self.codigo_conta_extra_orc = params['codigo_conta_extra_orc']
		self.desc_conta_extra_orc = params['desc_conta_extra_orc']
		self.data_referencia_doc = params['data_referencia_doc']
		self.vl_saldo_ini = params['vl_saldo_ini']

	@classmethod
	def save_multiple(cls, array):
		cls.session.add_all(array)
		cls.session.commit()

	@classmethod
	def all(cls):
		return cls.session.query(cls).all()

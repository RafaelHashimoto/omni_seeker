from sqlalchemy import Column, Float, Integer, String, DateTime
from models.base import Base


class DadoOrcamento(Base):
    __tablename__ = 'dados_orcamentos'

    id = Column(Integer, primary_key=True)
    codigo_municipio = Column(String)
    exercicio_orcamento = Column(String)
    nu_lei_orcamento = Column(String)
    valor_total_fixado_orcamento = Column(Float)
    numero_perc_sup_orcamento = Column(String)
    valor_total_supl_orcamento = Column(Float)
    data_envio_loa = Column(DateTime)
    data_aprov_loa = Column(DateTime)
    data_public_loa = Column(DateTime)

    def __init__(self, params):
        self.codigo_municipio = params['codigo_municipio']
        self.exercicio_orcamento = params['exercicio_orcamento']
        self.nu_lei_orcamento = params['nu_lei_orcamento']
        self.valor_total_fixado_orcamento = params['valor_total_fixado_orcamento']
        self.numero_perc_sup_orcamento = params['numero_perc_sup_orcamento']
        self.valor_total_supl_orcamento = params['valor_total_supl_orcamento']
        self.data_envio_loa = params['data_envio_loa']
        self.data_aprov_loa = params['data_aprov_loa']
        self.data_public_loa = params['data_public_loa']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()

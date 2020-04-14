from sqlalchemy import Column, Float, Integer, String
from models.base import Base


class Negociante(Base):
    __tablename__ = 'negociantes'

    id = Column(Integer, primary_key=True)
    numero_documento_negociante = Column(String)
    codigo_tipo_negociante = Column(String)
    nome_negociante = Column(String)
    endereco_negociante = Column(String)
    fone_negociante = Column(String)
    cep_negociante = Column(String)
    nome_municipio_negociante = Column(String)
    uf_negociante = Column(String)



    def __init__(self, params):
        self.numero_documento_negociante = params['numero_documento_negociante']
        self.codigo_tipo_negociante = params['codigo_tipo_negociante']
        self.nome_negociante = params['nome_negociante']
        self.endereco_negociante = params['endereco_negociante']
        self.fone_negociante = params['fone_negociante']
        self.cep_negociante = params['cep_negociante']
        self.nome_municipio_negociante = params['nome_municipio_negociante']
        self.uf_negociante = params['uf_negociante']

    @classmethod
    def save_multiple(cls, array):
        cls.session.add_all(array)
        cls.session.commit()

    @classmethod
    def all(cls):
        return cls.session.query(cls).all()

from sqlalchemy import create_engine, Column, String, Integer, Float, Date, ForeignKey, DECIMAL
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    cpf = Column('cpf', String, primary_key=True)
    nome = Column('nome', String)
    data_nascimento = Column('data_nascimento', Date)

    contas = relationship("Contas", back_populates="usuario")

    def __init__(self, nome,  cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Contas(Base):
    __tablename__ = 'contas'
    id = Column('id', Integer, primary_key=True)
    cpf = Column('cpf', String, ForeignKey('usuarios.cpf'))
    saldo = Column('saldo', DECIMAL(10, 2))
    numero_conta = Column('numero_conta', Integer)
    saques_diario_realizado = Column('saques_diario_realizado', Integer)
    tipo_conta = Column('tipo_conta', String)
    data_criacao = Column('data_criacao', Date, default=datetime.now().date)
    agencia = Column('agencia',String)
    limite_transacao_diaria = Column('limite_transacao_diaria',Integer)
    senha = Column('senha',String)

    usuario = relationship("Usuario", back_populates="contas")

    def __init__(self, cpf, saldo, numero_conta, saques_diario_realizado, tipo_conta,agencia,limite_transacao_diaria,senha):
        self.cpf = cpf
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.saques_diario_realizado = saques_diario_realizado
        self.limite_transacao_diaria = limite_transacao_diaria
        self.tipo_conta = tipo_conta
        self.agencia = agencia
        self.senha = senha

class Extrato(Base):
    __tablename__ = 'extratos'
    id = Column('id', Integer, primary_key=True)
    tipo = Column('tipo', String)
    valor = Column('valor', Float)
    data = Column('data', Date)
    id_conta = Column('id_conta', Integer, ForeignKey('contas.id'))

    def __init__(self, tipo, valor, data, id_conta):
        self.tipo = tipo
        self.valor = valor
        self.data = data
        self.id_conta = id_conta

Base.metadata.create_all(bind=db)

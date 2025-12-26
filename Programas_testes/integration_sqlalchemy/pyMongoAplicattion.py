from sqlalchemy import Column, Integer, String, ForeignKey, inspect, create_engine, select, func
from sqlalchemy.orm import declarative_base, relationship, Session

# Cria a base declarativa
base = declarative_base()


class User(base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)


    addresses = relationship("Address", back_populates="user", cascade='all, delete-orphan')

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, fullname={self.fullname})'


class Address(base):  # CORREÇÃO 3: Corrigido nome da classe de 'Adress' para 'Address'
    __tablename__ = 'address'  # Padronizei o nome da tabela também

    id = Column(Integer, primary_key=True)

    email = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'))


    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f'Address(id={self.id}, email={self.email})'


# Criando a conexão com o DB (SQLite em memória)
engine = create_engine('sqlite://') # cria apenas na memória ram

# Criando as tabelas
base.metadata.create_all(engine)

# Inspeção (opcional, para debug)
info_conexao_base = inspect(engine)
# print(info_conexao_base.get_table_names())

# Operações de Banco de Dados
with Session(engine) as sessao:
    juliana = User(
        name='Juliana',
        fullname='Da Silva',
        # Note que o atributo na classe User agora é 'addresses' (plural é boa prática para listas)
        addresses=[Address(email='juliana@gmail.com')]
    )
    gustavo = User(
        name='Gustavo',
        fullname='Maizatto',
        addresses=[Address(email='gustavo@gmail.com'), Address(email='yuken@gmail.com')]
    )

    # Enviar para o DB
    sessao.add_all([juliana, gustavo])
    sessao.commit()

    # Consultar dados

print("\n--- Resultado da Consulta ---")
stmt = select(User).where(User.id.in_([2,1])) # gera a expressão em SQL
for usuario in sessao.scalars(stmt):
    print(usuario)
        # Mostrando os endereços associados para provar que o relacionamento funcionou
    for addr in usuario.addresses:
        print(f"  -> E-mail: {addr.email}")

stmt_orderby = select(User).order_by(User.fullname.desc())
print(stmt_orderby)

print("\n--- Resultado da Consulta 2---")
# Recupera a informação do statment
for usuario in sessao.scalars(stmt_orderby):
    print(usuario)

print("\n--- Resultado da Consulta 3---")
stmt_join = select(User.fullname , Address.email, User.addresses).join_from(Address,User)
for usuario in sessao.scalars(stmt_join): #escalar, captura a 1° info
    print(usuario)


print("\n--- Resultado da Consulta 4---")
connection = engine.connect()
results = connection.execute(stmt_join).fetchall() # retorna em uma lista composta por tuplas
#results = connection.execute(stmt_join).fetchone() # retorna a tupla do primeior resultado apresentado
print(results)


print("\n--- Resultado da Consulta 5---")
stmt_count = select(func.count('*')).select_from(User)
print(stmt_count)
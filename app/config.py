from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = \
 '{SGBD}://{usuario}:{senha}@{servidor}/{database}?charset=utf8mb4'.format(
    SGBD = 'mysql+pymysql',
    usuario = 'root',
    senha = 'gabzz',
    servidor = '127.0.0.1',
    database = 'projetoldc'
)
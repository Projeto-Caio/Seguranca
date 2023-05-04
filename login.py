from dataclass import dataclass
from getpass import getpass
from hashlib import sha256

@dataclass
class Usuario:
    login: str
    senha: str

def pedir_login() -> Usuario:
    login = input('Digite seu Login: ')
    senha = getpass('Digite sua Senha: ')
    senha = sha256(senha.encode()).digest()
    return Usuario(login, senha)

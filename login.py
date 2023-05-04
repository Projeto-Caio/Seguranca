from dataclass import dataclass
from getpass import getpass
from hashlib import sha256
from repo import lista_usuarios

@dataclass
class Usuario:
    login: str
    senha: str

def pedir_login() -> Usuario:
    login = input('Digite seu Login: ')
    senha = getpass('Digite sua Senha: ')
    senha = sha256(senha.encode()).digest()
    return Usuario(login, senha)

def faz_login():
    usuarios = lista_usuarios()
    usuario = pedir_login()
    for usuario_salvo in usuarios:
        if usuario_salvo.login == usuario.login and usuario_salvo == usuario.senha:
            return usuario_salvo
    print('Usuário não encontrado')
    else None

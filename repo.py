from hashlib import sha256

def lista_usuarios():
    from login import Usuario
    return[
        Usuario(login='ettore', senha=sha256('Senha123'.encode).digest())
    ]
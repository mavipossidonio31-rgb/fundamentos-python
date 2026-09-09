def criar_email(nome, sobrenome, dominio):
    return nome.lower() + "." + sobrenome.lower() + "@" + dominio


nome = input("digite seu nome: ")
sobrenome = input("digite seu sobrenome: ")
dominio = input("digite o domínio: ")

print(criar_email(nome, sobrenome, dominio))
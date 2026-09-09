
# 1. Dividir uma string em partes

def separar_nome(nome_completo):
    partes = nome_completo.split()
    return partes

nome_completo = input("Digite seu nome completo: ")
partes = separar_nome(nome_completo)

# Usamos uma verificação para evitar erro caso o usuário digite menos de 3 palavras
if len(partes) >= 3:
    print(f"Terceira parte do nome: {partes[2]}")
else:
    print(f"Nome em partes: {partes}")


# 2. Juntar strings
def criar_nome_completo(partes):
    # Usando espaço em vez de vírgula para juntar nomes normalmente
    nome_completo = " ".join(partes)
    return nome_completo

partes_nome = ["joao", "renan", "celso"]
print(f"A junção das partes do nome é: {criar_nome_completo(partes_nome)}")


# 3. Verificar o início e o final de uma string

def analisar_url(url):
    inicio_com_https = url.startswith("https://")
    termina_com_br = url.endswith(".br")
    return inicio_com_https, termina_com_br

url = "https://www.gov.br"
tem_https, tem_br = analisar_url(url)
print(f"Utilizando https: {tem_https}")
print(f"Termina com .br? {tem_br}")

# 4. Verificar se a string contém somente números
def validar_idade(idade):
    if idade.isdigit():
        print("O valor digitado é uma idade válida (somente números).")
    else:
        print("Erro: digite somente números.")

idade = input("Digite sua idade: ")
validar_idade(idade)


# 5. Verificar se a string contém somente letras

def validar_nome(nome):
    # O método correto é isalpha()
    if nome.isalpha():
        print("O nome digitado é válido.")
    else:
        print("O nome deve conter somente letras.")

nome_usuario_input = input("Digite seu nome (somente letras): ")
validar_nome(nome_usuario_input)


# 6. Verificar se a string contém letras e números
def validar_usuario(usuario):
    # O método correto é isalnum() para letras e números
    if usuario.isalnum():
        print("O usuário digitado é válido.")
    else:
        print("Utilize apenas letras e números.")

nome_usuario = input("Digite seu nome de usuário: ")
validar_usuario(nome_usuario)


# 7. analisando uma frase
def analisar_frases(frase):
    frase_limpa = frase.strip().lower()

    qtde_caracteres = len(frase_limpa)
    qtde_caracteres2 = len(frase_limpa.split())
    ocorrencia_palavra = frase_limpa.count(palavra)

    print(f"frase completa: {frase_limpa}")
    print(f"total de caracteres: {qtde_caracteres}")
    print(f"total se palavras: {qtde_palavras}")
    print(f"ocorrencia: {ocorrencia_palavra}")

    frase_input = input("Digite uma frase: ")
    ocorrencia_palavra = input("Digite uma palavra:")
    analisar_frases(frase_input, ocorrencia_palavra)


    
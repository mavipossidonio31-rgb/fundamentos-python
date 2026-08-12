# Operadores and e or

def posso_entrar_no_show_do_veigh():
    POSSOIR_INGRESSO = True
    idade = int(input("Qual a sua idade? "))
    nome_esta_na_lista = bool(input(" seu nome esta na lista? "))

    posso_entrar = idade = nome_esta_na_lista or POSSOIR_INGRESSO and idade >= 18


    print(f"vou conseguir entrar no show? {posso_entrar}")

posso_entrar_no_show_do_veigh()
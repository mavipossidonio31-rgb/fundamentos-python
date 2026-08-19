# laço for simples
import time

def mostrar_numero():
    for i in range(1, 6):
        print(f"O número atual é {i}")
        time.sleep(5)

# mostrar_numero()


def mostrar_numero_aleatorio():
    for num in range(0, 20, 2):
        print(f"O número atual é {num}")

# mostrar_numero_aleatorio()


def somar_numeros():
    total = 0

    for valor in range(1, 20):
        total += valor

    print(total)


#somar_numeros()

def mostrar_numeros_pares():
    for numero in range(1, 21):
        if numero % 2 == 0:
            print(f"numero pares {numero}")

mostrar_numeros_pares()

#mostrar_numeros_pares()

def mostra_item_da_lista():
    sacola_de_frutas = ["maca", "banana","pare","abacate"]
    for fruta in sacola_de_frutas:
        print (f"na minha sacola contem {fruta}")

#mostra_item_da_lista


def  laco_aninhado():
    nomes = ["renam","moise","rafael"]
    notas =[8,9,10]
    for nome in nomes:
        print(f"nome do aluno {nome}")
        for nota in notas:
            print(f"nota do aluno {nota}")

laco_aninhado()

#mostrar_numero_while()
 def contagem_regressiva():
     valor_contagem = int(input("digite um numero maior que 10: "))
     if valor_contagem > 10:
         print("valor invalido")
     else:
         while valor_contagem > 1:
             print(f"contagem regressiva {valor_contagem}")
             valor_contagem -= 1
         print("decolando!!!!")

 contagem_regressiva()

#contagem_regressiva()

def soma_com_while():
    while True:
        num_1 = int(input("digite o primeiro valor: "))
        num_2=int(input("digite o segundo valor: "))

        if num_1==0:
            print("funçao de soma encerrada")
            break
        else:
        soma=num_1+num_2
        print(f"o resultado da soma e {soma}")


soma_com_while()



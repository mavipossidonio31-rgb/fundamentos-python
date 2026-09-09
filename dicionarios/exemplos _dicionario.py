#anatomia do dicionario
import json

from lista.exemplos_lista import calcular_media
from lista.exercicios.ex7 import quantidade


def exibir_alunos():
    alunos = {
        "nome": "carlos",
        "idade": 25,
        "curso": "desenvolvimento de sistema "
    }
    print('nome:',aluno["nome"])
    print('idade:',aluno{"idade"})
    print('curso:', aluno["curso"])
    print('nota :', aluno.get("nota"))''

    #exibir_alunos()


#atualizar valores
def atualizar_idade():
    aluno={
        "nome": "carlos",
        "idade": 25,
        "curso": "desenvolvimento de sistema "
    }

    print('idade antes:' , aluno.get('idade'))
    aluno['idade']=26
    print('idade atual:' , aluno.get('idade'))

    #atualizar_idade()

#adicionando novas informacoes
def adicionar_informacoes():
    aluno={
        "nome": "carlos",
        "idade":18
    }
    print('aluno antes:',aluno)
    aluno['curso']="tecnico em eletro_eletronica"
    aluno['nota']= 9.3
    print('aluno depois:',aluno)

#adicionar_informacoes()


#verificando se uma chave existe
def verificar_chave():
    aluno={
        "nome": "carlos",
        "idade": 25
    }

if'nome' in aluno:
    print('o nome esta cadastrado!')

    if 'nota' in aluno:
        print('o nota nao  esta cadastrada!')

        #verificar_chave()

#utilizando comparacoes
def verificar_aprovacao():
    aluno = {
        "nome": "carlos",
        "idade": 25,
        "nota": 9.5,
        "frequencia": 88
    }

if aluno ["nota"] >=6 and  aluno["frequencia"] >=75:
    print(f'o aluno {aluno["nome"]} esta aprovado!')
else:
    print(f'o aluno {aluno["nome"]} foi aprovado!')

#verificar_aprovacao()


#percorrendo as chaves
def listar_campos():
    produto = {
        "nome": "carlos",
        "quantidade": 50,
        "preco_unitario": 1.25
    }

    for chave in produto.keys():
        print(chave)

#listar_campos()

#percorrendo os valores
def listar_valores():
    produto = {
         "nome": "caneta azul"
         "quantidade": 50,
         "preco_unitario": 1.25
    }

    for valor in produto.values():
        print(valor)
#listar_valores()

#percorrendon chaves e valores
def exibir_produto():
    produto = {
        "nome": "morango",
        "quantidade": 50,
        "preco_unitario": 1.25
    }

    for chave,valor in produto.items():
        print(f'a chave {chave} tem o valor {valor}')

#exibir_produto()

#atualizando e calculando
def atualizar_estoque():
    produto = {
        "nome": "caneta azul"
        "quantidade": 50
        "preco_unitario": 1.25,
    }

    produto['total']=produto['quantidade']*produto['preco_unitario']
    print(produto)

    #atualizar_idade()

    #removendo elementos
    def remover_informacoes():
        produto = {
            "nome": "caneta azul"
            "quantidade": 50
            "preco_unitario": 1.25
        }

      #apaga da memoria do programa
    def produto['nome']
        #apaga e armazena  o item em outra variavel
        preco_unitario = produto.pop('preco_unitario')

        print(produto,preco_unitario)
 #remo

#lista de dicionarios
def listar_produtos():
    produto = [
        {"nome": "teclado","preco": 299,00, "quantidade": 2},
        {"nome": "mouse", "preco": 299,00, "quantidade": 3},
        {"nome": "monitor", "preco": 299,00, "quantidade": 1}

    ]

    for produto in produto:
        print(f"o produto{produto['nome']} tem o valor {produto['preco']}")
        total_individual = produto['preco'] * produto['quantidade']
        print(total_individual)



#listar_produtos()


#inserindo informacoes dinamicamente
def cadastrar_aluno():

    aluno = {

        aluno["nome"] = input ("digite o nome do aluno:")
        aluno["idade"] = input (int("digite o idade do aluno:"))
        aluno["curso"] = input ("digite o curso do aluno:")
        aluno["email"] = input ("digite o email:")
    }


def criar_cadastro():
    dados = {}

    quantidade = int(input("quantos dados vc deseja cadstrar:"))

    for item in range( 1, quantidade + 1 ):
        chave = input("digite o nome do campo:")
        valor = input("digite o valor da {chave}:")

        dados[chave] = valor

        print('cadastro final: ', dados )

#criar_cadastro()



#dicionario com lista
        def aluno_completo():
            aluno ={
                "nome": "renam",
                "idade":17,
                "curso": "desenvolvimento de sistema",
                "nota":[8.5,6.0,9.3,8.8],
                "endereco":{
                    "cidade": "piracicaba",
                    "rua":"rua dos cristais",
                    "numero": 1234,
                    "telefone":"(19)98272-5054"
                },
                "media":calcular_media('notas')
            }
        aluno['media'] = calcular_media(aluno['nota'])
        print(aluno)




 aluno ["media"]= calcular_media(aluno['nota'])
print(aluno['enderoco']["telefone"])

    #aluno_completo()
    def cadastrar_dados_aluno():
        aluno = {}

        aluno["nome"] = input ("digite o nome do aluno:")
        aluno["idade"]=input("digite o idade do aluno:")
        aluno["curso"] = input ("digite o curso do aluno:")
        aluno["nota"]= []

        for nota in range (4):
            aluno["notas"].append(float(input("digite a nota{nota+1}:")))

            aluno["endereco"] = {}
            aluno["endereco"]["cidade"] = input ("digite o cidade do endereco:")
            aluno["endereco"]["rua"] = input ("digite o rua do endereco:")
            aluno["endereco"]["numero"] = input(input ("digite o numero da casa:"))
            aluno ["endereco"]["telefone"] = input ("digite telefone ddd:")

            aluno["media"] = calcular_media(aluno["nota"])
            print("aluno cadastrado", json.dumps(aluno, indent=4))

            cadastrar_dados_aluno()





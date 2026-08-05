
def exibir_mensagem():
    print("hello world!!!!!!! \n"*30)

def somar():
    valor1=50
    valor2=60
    total=valor1+valor2
    print(f"o resultado da soma e {total}")

def calcular_media():
    nota1=float(input("digita a nota da primeira prova:"))
    nota2=float(input("digite a nota da segunda prova:"))
    media=(nota1+nota2)/2
    return media

exibir_mensagem()
somar()

nota_final =calcular_media()
print(f"a nota final da soma e {nota_final}")
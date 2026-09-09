#coverter texto para maiusculo e minusculo
def formatar_nome(nome):
    nome_maiusculo = nome.upper()

    #nome minuscolo:
    nome_minusculo = nome.lower()

    #nome com primeira letra maiuscula:
    nome_camel_case = nome.capitalize()

    return( nome_maiusculo, nome_minusculo, nome_camel_case)

nomes= input("Digite seu nome : ")

print(f"nome maiusculo: {formatar_nome(nomes)}")

#print (formato_nome(nome)[1])

banana, batata = formato_nome(nome)
print(f"nome maiusculo: {nome_minusculo}"
print(f"nome minuscolo: {nome_maiuscolo}")

#remover espaços desnecessarios
def limpar_texto(texto):
    #remover espacços no inicio e final don texto
    texto_limpo= texto.strip()
    return texto_limpo

print(f"texto antes: {texto_1}")

banana,batata,cebola = for

#substituir palavra
def trocar_cidade(texto):
    #trocar uma palavra por outra
    texto_trocado = texto.replace("sao paulo ","piracicaba")
    return texto_trocado

  cidade= "eu moro em sao paulo"
  print(trocar_cidade(cidade))

  cidade = input("digite a cidade que vc mora:")
  print(f"eu moro em :{trocar_cidade(cidade)}")

  #contar caracteres ou ocorrencias
  def analisar_texto(texto):


    #contar a quantidade de ocorrencias
   qtde_letra_a = texto.strip().lower().count('letra')

    return qtde_caracteres,qtde_letra_a

 texto_2 = input("Digite um texto: ")
 letra = input("Digite uma letra: ")
 caracteres, letras = analisar_texto(texto_2, letra)

 print(f"total de caracteres em letras: {caracteres}")
 print(f"total de letras em pesquisadas: {letras}")

 #verificar se uma palvra esta presente
 def verficar_palavra(frase,palavra):
palavra_presente = palavra.lower() in frase.lower()
return palavra_presente


#encontrar a posicao de uma palavra

   def encontrar_posicao_palavra(frase,palavra):
    posicao_palavra = frase.lower().find(palavra.lower())
    return posicao_palavra

   frse_2= input("Digite uma frase: ")
   palavra_2= input("Digite uma palavra para saber sua posicao: ")

   print(f"a posicao da palavra e {encontrar_posicao_palavra(frase,palavra_2)}")

   



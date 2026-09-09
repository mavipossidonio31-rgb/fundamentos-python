def validar_especie(animal):

    if animal.isalpha():
        print("espécie de animal válida.")
    else:
        print("espécie inválida.")


animal = input("digite o nome do animal: ")

validar_especie(animal)
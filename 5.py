def telefone ():

    numero = input("Digite seu numero de telefone: ")

    if len(numero) == 9:
        print(f"Sua numero e: {numero}")
    else:
        print("Esta faltando o nove na frente")

telefone()   
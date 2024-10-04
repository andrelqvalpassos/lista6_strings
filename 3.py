def altera_data ():

    data_nascimento = input("Digite sua data de nascimento no formato (dia/mes/ano): ")

    if "/" in data_nascimento:
        partes  = data_nascimento.split('/')
        if len(partes) == 3:
            dia = partes[0]
            mes = partes [1]
            ano = partes [2]
            print(f"Voce nasceu no dia {dia} do mes {mes} e ano {ano}")
        else:
            print("Data invalida")
    else:
        print("Data invalida")

altera_data()   
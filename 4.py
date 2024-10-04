def nova_senha ():

    data_nascimento = input("Digite sua data de nascimento no formato (dia/mes/ano): ")

    if "/" in data_nascimento:
        partes  = data_nascimento.split('/')
        if len(partes) == 3:
            dia = partes[0]
            mes = partes [1]
            ano = partes [2]
            print(f"Sua senha e: {mes}${dia}#{dia}!{mes}*{ano}")
        else:
            print("Senha invalida")
    else:
        print("Senha invalida")

nova_senha()   
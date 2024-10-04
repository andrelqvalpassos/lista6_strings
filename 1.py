def verifica_email ():
    email = input("Digite seu email: ")

    if "@" in email:
        print("Email valido")
    else:
        print("Email não valido")

verifica_email()
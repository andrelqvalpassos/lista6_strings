def subs_palavra():
    lista_palavras = []

    # Solicita a frase do usuário
    frase = input("Digite uma frase: ")

    # Divide a frase em uma lista de palavras
    lista_palavras = frase.split()  # A função split() separa as palavras por espaços

    # Exibe a lista de palavras original
    print(f"Lista original de palavras: {lista_palavras}")

    # Solicita uma nova palavra para substituir a última palavra
    nova_palavra = input("Digite uma palavra para substituir a última palavra da lista: ")

    # Substitui a última palavra
    lista_palavras[-1] = nova_palavra  # O índice -1 refere-se ao último elemento da lista

    # Exibe a lista modificada
    print(f"Lista modificada de palavras: {lista_palavras}")

subs_palavra()

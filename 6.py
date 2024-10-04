def situacao_aluno():
    # Inicializa listas para armazenar nomes e médias
    nomes = []
    medias = []

    # Laço para capturar os dados de 3 alunos
    for i in range(3):
        # Solicita o nome do aluno
        nome_aluno = input(f"Digite o nome do aluno {i + 1}: ")
        nomes.append(nome_aluno)  # Armazena o nome na lista
        
        # Solicita as três notas do aluno e calcula a média
        notas = []
        for j in range(3):
            nota = float(input(f"Digite a {j + 1}ª nota do aluno {nome_aluno}: "))
            notas.append(nota)
        
        media_aluno = sum(notas) / 3  # Calcula a média
        medias.append(media_aluno)  # Armazena a média na lista

    # Exibe os nomes e as médias dos alunos
    for i in range(3):
        print(f"\nNome do aluno: {nomes[i]}")
        print(f"Média: {medias[i]:.2f}")


        if medias[i] >= 7:
            print("Aprovado")
        else:
            print("Reprovado")

# Chama a função para executar o programa
situacao_aluno()

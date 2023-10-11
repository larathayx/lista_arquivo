def calcular_idade_media(estudantes):
    total_idades = 0
    numero_de_estudantes = len(estudantes)
    
    for estudante in estudantes:
        total_idades += int(estudante["Idade"])
    
    if numero_de_estudantes > 0:
        idade_media = total_idades / numero_de_estudantes
    else:
        idade_media = 0
    
    return idade_media

estudantes = []

with open('estudantes.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split(', ')
        estudante = {}
        for parte in partes:
            chave, valor = parte.split(': ')
            estudante[chave] = valor
        estudantes.append(estudante)

idade_media = calcular_idade_media(estudantes)

print(f'A idade média dos estudantes é: {idade_media} anos')

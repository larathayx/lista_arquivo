def procurar_estudante(nome, estudantes):
    for estudante in estudantes:
        if estudante["Nome"].lower() == nome.lower():
            return estudante
    return None

estudantes = []
with open('estudantes.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split(', ')
        estudante = {}
        for parte in partes:
            chave, valor = parte.split(': ')
            estudante[chave] = valor
        estudantes.append(estudante)

while True:
    nome_busca = input("Digite o nome do estudante que deseja encontrar (ou 'sair' para encerrar): ")
    
    if nome_busca == 'sair':
        break
    
    estudante_encontrado = procurar_estudante(nome_busca, estudantes)
    if estudante_encontrado:
        print(f'Nome: {estudante_encontrado["Nome"]}')
        print(f'Idade: {estudante_encontrado["Idade"]}')
        print(f'Curso: {estudante_encontrado["Curso"]}')
    else:
        print(f'Estudante com o nome "{nome_busca}" não encontrado.')
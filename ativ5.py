def remover_estudante(nome, estudantes):
    estudantes_copia = estudantes.copy()
    removido = False
    for estudante in estudantes_copia:
        if estudante["Nome"] == nome:
            estudantes.remove(estudante)
            removido = True
    return removido

def atualizar_arquivo(estudantes):
    with open('estudantes.txt', 'w') as arquivo:
        for estudante in estudantes:
            arquivo.write(f'Nome: {estudante["Nome"]}, Idade: {estudante["Idade"]}, Curso: {estudante["Curso"]}\n')

estudantes = []

with open('estudantes.txt', 'r') as arquivo:
    for linha in arquivo:
        estudante_info = {}
        partes = linha.strip().split(', ')
        for parte in partes:
            chave, valor = parte.split(': ')
            estudante_info[chave] = valor
        estudantes.append(estudante_info)

while True:
    nome_remover = input("Digite o nome do estudante a ser removido (ou 'sair' para encerrar): ")
    if nome_remover == 'sair':
        break
    
    if remover_estudante(nome_remover, estudantes):
        print(f'O estudante com o nome "{nome_remover}" foi removido com sucesso.')
        atualizar_arquivo(estudantes)
    else:
        print(f'Estudante com o nome "{nome_remover}" não encontrado.')

def contar_estudantes_por_curso(estudantes):
    contagem_por_curso = {}
    
    for estudante in estudantes:
        curso = estudante["Curso"]
        if curso in contagem_por_curso:
            contagem_por_curso[curso] += 1
        else:
            contagem_por_curso[curso] = 1
    
    return contagem_por_curso

estudantes = []

with open('estudantes.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.strip().split(', ')
        estudante = {}
        for parte in partes:
            chave, valor = parte.split(': ')
            estudante[chave] = valor
        estudantes.append(estudante)

contagem_cursos = contar_estudantes_por_curso(estudantes)

for curso, contagem in contagem_cursos.items():
    print(f'Curso: {curso}, Estudantes Matriculados: {contagem}')

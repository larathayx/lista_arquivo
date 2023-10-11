quant = int(input("Digite a quantidade de estudantes que você quer na lista: "))
estudantes = []

for x in range(quant):
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    curso = input("Digite o curso: ")
    
    estudante_info = {
        'Nome': nome,
        'Idade': idade,
        'Curso': curso
    }
    
    estudantes.append(estudante_info)

with open('estudantes.txt', 'w') as arquivo:
    for estudante in estudantes:
        arquivo.write(f"Nome: {estudante['Nome']}, Idade: {estudante['Idade']}, Curso: {estudante['Curso']}\n")



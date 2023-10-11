def atualizar_estudante(estudante, campo, novo_valor):
    if campo == 'Nome':
        estudante['Nome'] = novo_valor
    elif campo == 'Idade':
        estudante['Idade'] = novo_valor
    elif campo == 'Curso':
        estudante['Curso'] = novo_valor

estudantes = []
with open('estudantes.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.strip().split(', ')
        nome = partes[0].split(': ')[1]
        idade = partes[1].split(': ')[1]
        curso = partes[2].split(': ')[1]
        
        estudante_info = {
            'Nome': nome,
            'Idade': idade,
            'Curso': curso
        }
        
        estudantes.append(estudante_info)

nome_para_atualizar = input("Digite o nome do estudante que você deseja atualizar: ")
encontrado = False

for estudante in estudantes:
    if estudante['Nome'] == nome_para_atualizar:
        encontrado = True
        break

if encontrado:
    campo_para_atualizar = input(f"Digite o campo que você deseja atualizar para {nome_para_atualizar} (Nome, Idade, ou Curso): ").capitalize()
    
    if campo_para_atualizar in ['Nome', 'Idade', 'Curso']:
        novo_valor = input(f"Digite o novo valor para {campo_para_atualizar}: ")
        atualizar_estudante(estudante, campo_para_atualizar, novo_valor)
        
        with open('estudantes.txt', 'w') as arquivo:
            for e in estudantes:
                arquivo.write(f"Nome: {e['Nome']}, Idade: {e['Idade']}, Curso: {e['Curso']}\n")
        
        print(f"{campo_para_atualizar} de {nome_para_atualizar} foi atualizado com sucesso!")
    else:
        print("Campo inválido. Por favor, digite 'Nome', 'Idade' ou 'Curso'.")
else:
    print(f"{nome_para_atualizar} não foi encontrado na lista de estudantes.")

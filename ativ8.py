quant = int(input("Digite a quantidade de contatos que você quer na lista: "))
contatos = []

for x in range(quant):
    nome = input("Digite o nome: ")
    numero = input("Digite o número: ")

    dados = {
        'Nome': nome,
        'Numero': numero,
    }

    contatos.append(dados)

with open('contatos.txt', 'w') as arquivo:
    for contact in contatos:
        arquivo.write(f"Nome: {contact['Nome']}, Numero: {contact['Numero']}\n")

with open('contatos.txt', 'r') as arquiv:
    conteudo = arquiv.read()
    print(conteudo)

atualiza = input("Deseja atualizar algum dado? (s/n) ")
if atualiza == 's':
    def atualizar_contato(contato, campo, novo_valor):
        if campo == 'Nome':
            contato['Nome'] = novo_valor
        elif campo == 'Numero':
            contato['Numero'] = novo_valor

    with open('contatos.txt', 'r') as arquivo:
        contatos = []
        for linha in arquivo:
            partes = linha.strip().split(', ')
            nome = partes[0].split(': ')[1]
            numero = partes[1].split(': ')[1]

            dados = {
                'Nome': nome,
                'Numero': numero,
            }

            contatos.append(dados)

    nome_para_atualizar = input("Digite o nome do contato que você deseja atualizar: ")
    encontrado = False

    for contato in contatos:
        if contato['Nome'] == nome_para_atualizar:
            encontrado = True
            break

    if encontrado:
        campo_para_atualizar = input(f"Digite o campo que você deseja atualizar para {nome_para_atualizar} (Nome ou Numero): ").capitalize()

        if campo_para_atualizar in ['Nome', 'Numero']:
            novo_valor = input(f"Digite o novo valor para {campo_para_atualizar}: ")
            atualizar_contato(contato, campo_para_atualizar, novo_valor)

            with open('contatos.txt', 'w') as arquivo:
                for e in contatos:
                    arquivo.write(f"Nome: {e['Nome']}, Numero: {e['Numero']}\n")

            print(f"{campo_para_atualizar} de {nome_para_atualizar} foi atualizado com sucesso!")
        else:
            print("Campo inválido. Por favor, digite 'Nome' ou 'Numero'.")
    else:
        print(f"{nome_para_atualizar} não foi encontrado na lista de contatos.")

def procurar_nome(nome, contatos):
    for contato in contatos:
        if contato["Nome"] == nome:
            return contato
    return None

while True:
    nome_busca = input("Digite o nome do contato que deseja encontrar (ou 'sair' para encerrar): ")

    if nome_busca == 'sair':
        break

    contato_encontrado = procurar_nome(nome_busca, contatos)

    if contato_encontrado:
        print(f'Nome: {contato_encontrado["Nome"]}')
        print(f'Numero: {contato_encontrado["Numero"]}')
    else:
        print(f'Contato com o nome "{nome_busca}" não encontrado.')

def remover_contato(nome, contatos):
    for contato in contatos:
        if contato["Nome"] == nome:
            contatos.remove(contato)
            return True
    return False

def atualizar_arquivo(contatos):
    with open('contatos.txt', 'w') as arquivo:
        for contato in contatos:
            arquivo.write(f'Nome: {contato["Nome"]}, Numero: {contato["Numero"]}\n')

while True:
    nome_remover = input("Digite o nome do contato a ser removido (ou 'sair' para encerrar): ")
    if nome_remover == 'sair':
        break

    if remover_contato(nome_remover, contatos):
        print(f'O contato com o nome "{nome_remover}" foi removido com sucesso.')
        atualizar_arquivo(contatos)
    else:
        print(f'Contato com o nome "{nome_remover}" não encontrado.')

def adicionar_contato(contatos):
    nome = input("Digite o nome: ")
    numero = input("Digite o número: ")

    novo_contato = {
        'Nome': nome,
        'Numero': numero,
    }

    contatos.append(novo_contato)

    with open('contatos.txt', 'a') as arquivo: 
        arquivo.write(f"Nome: {novo_contato['Nome']}, Numero: {novo_contato['Numero']}\n")

while True:
    resposta = input("Deseja adicionar um novo contato? (s/n): ")
    if resposta.lower() != 's':
        break
    adicionar_contato(contatos)
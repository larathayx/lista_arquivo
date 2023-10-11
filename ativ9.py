def salvar_produtos_em_arquivo(produtos):
    with open('produtos_valor.txt', 'w') as arquivo:
        for produto in produtos:
            arquivo.write(f"Nome: {produto['Nome']}, Valor: {produto['Valor']}\n")

def adicionar_produto(produtos):
    nome = input("Digite o nome do produto: ")
    valor = input("Digite o valor: ")

    novo_produto = {
        'Nome': nome,
        'Valor': valor,
    }

    produtos.append(novo_produto)

    salvar_produtos_em_arquivo(produtos)

def atualizar_dado(produto, campo, novo_valor):
    if campo == 'Nome':
        produto['Nome'] = novo_valor
    elif campo == 'Valor':
        produto['Valor'] = novo_valor

produtos = []

quant = int(input("Digite a quantidade de produtos que você quer na lista: "))

for _ in range(quant):
    nome = input("Digite o nome do produto: ")
    valor = input("Digite o valor: ")

    dados = {
        'Nome': nome,
        'Valor': valor,
    }

    produtos.append(dados)

salvar_produtos_em_arquivo(produtos)

while True:
    resposta = input("Deseja adicionar um novo produto? (s/n): ")
    if resposta.lower() != 's':
        break
    adicionar_produto(produtos)

atualiza = input("Deseja atualizar algum dado? (s/n) ")
if atualiza == 's':
    with open('produtos_valor.txt', 'r') as arquivo:
        produtos = []
        for linha in arquivo:
            partes = linha.strip().split(', ')
            nome = partes[0].split(': ')[1]
            valor = partes[1].split(': ')[1]

            dados = {
                'Nome': nome,
                'Valor': valor,
            }

            produtos.append(dados)

    nome_para_atualizar = input("Digite o nome do produto que você deseja atualizar: ")
    encontrado = False

    for produto in produtos:
        if produto['Nome'] == nome_para_atualizar:
            encontrado = True
            break

    if encontrado:
        campo_para_atualizar = input(f"Digite o campo que você deseja atualizar para {nome_para_atualizar} (Nome ou Valor): ").capitalize()

        if campo_para_atualizar in ['Nome', 'Valor']:
            novo_valor = input(f"Digite o novo valor para {campo_para_atualizar}: ")
            atualizar_dado(produto, campo_para_atualizar, novo_valor)

            salvar_produtos_em_arquivo(produtos)

            print(f"{campo_para_atualizar} de {nome_para_atualizar} foi atualizado com sucesso!")
        else:
            print("Campo inválido. Por favor, digite 'Nome' ou 'Valor'.")
    else:
        print(f"{nome_para_atualizar} não foi encontrado na lista de produtos.")

def calcular_valor_total(produtos):
    total = 0
    for produto in produtos:
        valor = float(produto['Valor']) 
        total += valor
    return total

total = calcular_valor_total(produtos)
print(f"O valor total dos produtos é: R$ {total}")
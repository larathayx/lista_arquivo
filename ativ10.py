import csv

nome_arquivo_csv = 'compras.csv'
nome_arquivo_txt = 'produtos_valor.txt'

try:
    with open(nome_arquivo_txt, 'r') as arquivo_txt, open(nome_arquivo_csv, 'w', newline='') as arquivo_csv:
        leitor_txt = csv.reader(arquivo_txt)
        escritor_csv = csv.writer(arquivo_csv)
        
        for linha in leitor_txt:
            escritor_csv.writerow(linha)

    print(f'Os dados foram lidos do arquivo "{nome_arquivo_txt}" e gravados em "{nome_arquivo_csv}".')
except FileNotFoundError:
    print(f"O arquivo de texto '{nome_arquivo_txt}' não foi encontrado.")

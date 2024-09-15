

# Passo 03: Tratar/compilar as bases de dados
# Passo 04: Calcular o produto mais vendido (em quantidade)
# Passo 05: Calcular o produto que mais faturou (em faturamento)
# Passo 06: Calcular a loja que mais vendeu (em faturamento) - Criar um Dashboard

# Passo 01: Percorrer todos os arquivos da pasta da base de dados (Vendas)
import os
lista_arquivo = os.listdir("Vendas")
lista_ordenada = sorted(lista_arquivo)

for arquivo in lista_ordenada:
    print(arquivo)

# Passo 02: Importar as bases de dados de vendas


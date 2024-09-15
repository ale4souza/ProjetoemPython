import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Listar arquivos no diretório "Vendas"
lista_arquivo = os.listdir("Vendas")

# Ordenar a lista de arquivos
lista_ordenada = sorted(lista_arquivo)

# Inicializar uma lista para armazenar as tabelas
tabela_total = []

# Passo 02: Importar as bases de dados de vendas
for arquivo in lista_ordenada:
    caminho_arquivo = os.path.join("Vendas", arquivo)  # Construir o caminho completo do arquivo
    if "vendas" in arquivo.lower() and arquivo.endswith(".csv"):
        # Ler o arquivo CSV e adicionar à lista de tabelas
        tabela = pd.read_csv(caminho_arquivo)
        tabela_total.append(tabela)
        
#print(tabela_total)

# Concatenar todas as tabelas em um único DataFrame
tabela_total = pd.concat(tabela_total)
print(tabela_total) # Exibir o DataFrame consolidado

# Calcular produto mais vendido em quantidades
tabela_produto = tabela_total.groupby("Produto")["Quantidade Vendida"].sum()
tabela_produto = tabela_produto.sort_values(ascending=False)

#criando uma nova coluna

tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
#print(tabela_total)

tabela_faturamento = tabela_total.groupby("Produto")["Faturamento"].sum()

# Calcular produto mais vendido em faturamento
tabela_faturamento = tabela_faturamento.sort_values(ascending=False)
print(tabela_faturamento)

#Calcular a loja/cidade que mais faturou

tabela_loja= tabela_total.groupby("Loja")["Faturamento"].sum()
tabela_loja= tabela_loja.sort_values(ascending=False)
print (tabela_loja)

# Criar o gráfico de barras
grafico = px.bar(
    tabela_loja,
    x=tabela_loja.index,  # Nomes das lojas
    y=tabela_loja.values,  # Valores de faturamento
    title="Faturamento por Loja",  # Título do gráfico
    labels={"x": "Lojas", "y": "Faturamento"},  # Rótulos dos eixos
    color_discrete_sequence=["#1f77b4"],  # Definir uma cor personalizada
)

# Personalizar a aparência do gráfico
grafico.update_layout(
    xaxis_title="Lojas",  # Rótulo do eixo X
    yaxis_title="Faturamento (R$)",  # Rótulo do eixo Y
    title_font_size=24,  # Tamanho da fonte do título
    xaxis_tickangle=-45,  # Girar os rótulos do eixo X
    template="plotly_white"  # Usar um tema mais claro
)

# Formatando o eixo Y para exibir os valores em reais (R$)
grafico.update_yaxes(
    tickprefix="R$",  # Prefixo para os valores (R$)
    tickformat=".2f"  # Formatar com 2 casas decimais
)

# Exibir o gráfico
grafico.show()

import pandas as pd 
from pathlib import Path
from  tabulate import tabulate
# dataframe = pd.DataFrame()
def show_table(table):
    print(tabulate(table,  headers= 'keys', tablefmt='fancy_grid'))

BASE_DIR = Path(__file__).resolve().parent

VENDAS_DIR = BASE_DIR / 'excel_folder' / 'Vendas#.xlsx'
VENDAS_DEZ_DIR = BASE_DIR / 'excel_folder' / 'Vendas - Dez#.xlsx'
GERENTES_DIR = BASE_DIR / 'excel_folder'/'Gerentes#.xlsx'

venda = {
    'data': ['15/02/2021', '23/05/2022'],
    'valor': [500, 300],
    'produto': ['frango', 'carne'],
    'qtde':[43, 76]
}
vendas_df = pd.DataFrame(venda)
show_table(vendas_df.describe())

vendas_df = pd.read_excel(VENDAS_DIR)
show_table(vendas_df.head(20))
print(vendas_df.shape)
show_table(vendas_df[['Produto', 'Quantidade']])

""" Filtrando Colunas com Base em uma condição específica .loc[linha,coluna]"""

show_table(vendas_df.loc[8:13])
vendas_rio_mar_shopping = vendas_df.loc[vendas_df['ID Loja'] == 'Rio Mar Shopping Fortaleza']
show_table(vendas_rio_mar_shopping)
vendas_calca = vendas_df.loc[vendas_df['Produto'] == 'Calça', ['ID Loja', 'Produto', 'Valor Unitário']]
show_table(vendas_calca)

""" Adicionando uma nova Coluna"""
# A partir de uma coluna que já existe
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
show_table(vendas_df.head(10))

# Com um valor padrão
# no pandas ":"  é igual a todas
vendas_df.loc[:, 'Imposto'] = 0 # Na coluna de imposto vai ser preenchido todas as linhas com o valor 0
show_table(vendas_df.head(10))

vendas_dez_df = pd.read_excel(VENDAS_DEZ_DIR)
show_table(vendas_dez_df)

""" Concatenar duas tabelas """
vendas_df = pd.concat([vendas_df,vendas_dez_df], ignore_index=True)
show_table(vendas_df.tail(10))
print(vendas_df.shape)

""" Excluir Coluna"""
vendas_df = vendas_df.drop('Imposto', axis=1) #axis=0 é igual a row e axis=1 é igual a column
vendas_df = vendas_df.drop(0, axis=0) # Deletando a row 0
show_table(vendas_df.head(10))

""" Deletar Rows or Coluns que estão vazias"""
# Deletar a coluna(axis=1) se todos(all) os valores forem vazios(nan)
vendas_df = vendas_df.dropna(how='all', axis=1)

# # (DEFAULT) Deleta a linha(axis=0) se pelo menos algum(any) um dos valores forem vazias
vendas_df = vendas_df.dropna() # o default é isso vendas_df.dropna(how='any', axis=0)

""" Preencher Rows or Coluns que estão vazias"""
# Preenchendo as rows vazias com a média(mean) da coluna comissão
vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean()) 
print(vendas_df)

""" Value Counts"""
# Basicamente vai contar quantas vezes cada dado se repetiu e vai colocar a coluna do lado da contagem total de cada dado
transaçoes_loja = vendas_df['ID Loja'].value_counts() 
print(transaçoes_loja)

# """ Group By"""
faturamento_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum()
show_table(faturamento_produto)

""" Mesclar 2 DataFrames"""
gerentes_df = pd.read_excel(GERENTES_DIR)
vendas_df = vendas_df.merge(gerentes_df)
show_table(vendas_df)
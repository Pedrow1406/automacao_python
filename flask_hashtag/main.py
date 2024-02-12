import requests, json

response = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')

dolar = response.json()['USDBRL']['bid']
euro = response.json()['EURBRL']['bid']
bitcoin = response.json()['BTCBRL']['bid']
print(response.json())
print()
print(f'1 Dólar Americado equivale a {dolar} Reais Brasileiros')
print(f'1 Euro equivale a {euro} Reais Brasileiros')
print(f'1 Bitcoin equivale a {bitcoin} Reais Brasileiros')
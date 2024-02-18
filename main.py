from automacao import acessar_youtube
from datetime import datetime
def triangle(quantidade):
    for column in range(1,quantidade+1):
        print('*' * column)

def two_fors_triangle(quantidade):
    for x in range(quantidade):
        for y in range(x + 1):
            print('*', end = '')
        print()

def tree(quantidade):
    i = 0
    for c in range(1, quantidade + 1):
        mult = '*' * i
        string = '*' * c + mult
        print(string.center(quantidade * 2))
        i += 1
    print('*'.center(quantidade * 2))

def tree_inversed(quantidade):
    i = quantidade
    print('*'.center(quantidade * 2 + 1))
    for c in range(quantidade + 1, 0, -1):
        mult = '*' * i
        string = '*' * c + mult
        print(string.center(quantidade * 2 + 1))
        i -= 1
def busca_elemento_lista(elemento):
    lista = [3, 5, 2, 1, 7, 4, 3, 2, 1, 9 ]
    for i, l in enumerate(lista):
        if l == elemento:
            return i
        

def days_remaining(day, month, year=datetime.now().year):
    target_date = datetime(day=day, month=month, year=year)
    current_date = datetime.now()
    remaining = target_date - current_date
    day_remaining = remaining.days
    
    day = str(day).zfill(2) # Adiciona zeros a esquerda para se adaptar a quantidade de algarismos passado como parâmetro. Ex: '13'.zfill(4) == '0013' 
    month = str(month).zfill(2)
    print(f'Restam {day_remaining} dias para {day}/{month}/{year}')


days_remaining(18, 3)
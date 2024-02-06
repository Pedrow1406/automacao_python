from automacao import acessar_youtube

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
        
tree(10)
print()
print()
tree_inversed(10)
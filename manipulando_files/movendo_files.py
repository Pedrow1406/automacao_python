import os 

dir_vendas = r'C:\Users\apfri\Pictures\Desktop\historico_vends'

def formata_mes(mes, venda, extensao):
    if mes not in venda:
        venda = venda.split(' ')
        for i in range(len(venda)):
            if mes in venda[i].lower():
                venda[i] = mes + extensao
                break
        venda = ' '.join(venda)
        return venda
    return venda
    
for venda in os.listdir(dir_vendas):
    mes = None
    nome_completo = os.path.join(dir_vendas, venda)
    if '.' in venda:
        i_ext = venda.index('.')
        ext = venda[i_ext:]
        if ext in venda:
            if 'jan' in venda.lower():
                mes = 'Jan'
                venda = formata_mes('jan', venda, ext)
                print(venda)

            elif 'fev' in venda.lower():
                mes = 'Fev'
                venda = formata_mes('fev', venda, ext)
                print(venda)
                
            elif 'mar' in venda.lower(): 
                mes = 'Mar'
                venda = formata_mes('mar', venda, ext)
                print(venda)
    
    if mes:
        nome_completo_novo = os.path.join(dir_vendas, mes, venda)
        os.rename(nome_completo, nome_completo_novo)
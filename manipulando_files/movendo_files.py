import os 

dir_vendas = r'C:\Users\apfri\Pictures\Desktop\historico_vends'

def formata_mes(mes, venda, extensao):
    venda = venda.split(' ')
    for i in range(len(venda)):
        if mes in venda[i].lower():
            venda[i] = mes + extensao
            break
    venda = ' '.join(venda)
    return venda

meses = ['jan', 'fev', 'mar','abr', 'mai', 'jun', 'jul', 'ago', 'set','out', 'nov', 'dez']  
for venda in os.listdir(dir_vendas):
    mes = None
    nome_completo = os.path.join(dir_vendas, venda)
    if '.' in venda:
        i_ext = venda.index('.')
        ext = venda[i_ext:]     
        if ext in venda:
            for m in meses:
                if m in venda.lower():
                    mes = m.capitalize()
                    venda = formata_mes(m, venda, ext)
                    print(venda)
                    break
    if mes:
        dir_vendas_mes = os.path.join(dir_vendas, mes)
        if not os.path.exists(dir_vendas_mes): # Verifica se esse diretório não existe
            os.mkdir(dir_vendas_mes) # Cria um diretório novo caso ele não exista
        nome_completo_novo = os.path.join(dir_vendas_mes, venda)
        os.rename(nome_completo, nome_completo_novo)
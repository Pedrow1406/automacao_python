import openpyxl
from PIL import Image, ImageDraw, ImageFont
workbook = openpyxl.load_workbook('dev-aprender/planilha_alunos.xlsx')
sheet_alunos = workbook['Sheet1']

for i, row in enumerate(sheet_alunos.iter_rows(min_row=2, max_row=21, values_only=True)): 
    nome = row[1]
    curso = row[0]
    participacao = row[2]
    carga_horaria = str(row[5])
    inicio = row[3]
    termino = row[4]
    emissao = row[-1]

    font_nome  = ImageFont.truetype(r'dev-aprender\tahomabd.ttf', 80)
    font_geral = ImageFont.truetype(r'dev-aprender\tahoma.ttf', 80)
    font_data = ImageFont.truetype(r'dev-aprender\tahoma.ttf', 60)
    image = Image.open('dev-aprender\certificado_padrao.jpg')

    draw = ImageDraw.Draw(image)

    draw.text((1030, 840), nome, fill='black', font=font_nome)
    draw.text((1080, 955), curso, fill='black', font=font_geral)
    draw.text((1450, 1070), participacao, fill='black', font=font_geral)
    draw.text((1510, 1190), carga_horaria, fill='black', font=font_geral)
    draw.text((735, 1780), inicio, fill='blue', font=font_data)
    draw.text((735, 1927), termino, fill='blue', font=font_data)
    draw.text((2210,1927), emissao, fill='blue', font=font_data)
    nome_pessoa = nome.split(' ')[0]
    sobrenome_pessoa = nome.split(' ')[1]

    nome_pessoa = f'{nome_pessoa}_{sobrenome_pessoa}'
    print(nome_pessoa)
    image.save(fr'dev-aprender/certificados/{i+1}_{nome_pessoa}.png')
    
    print(f'Nome: {nome}')
    print(f'Curso: {curso}')
    print(f'Participação: {participacao}')
    print(f'Carga Horária: {carga_horaria}')
    print(f'Início: {inicio}')
    print(f'Termino: {termino}')
    print(f'Emissão: {emissao}')
    print()
    
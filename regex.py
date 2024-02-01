import re
string = "Pedrow Melo1406"
pattern = re.compile(r"[a-zA-Z\s0-3]")
x = re.findall(pattern, string)
print(x)
pattern = re.compile(r"[\w\s]")
x = re.findall(pattern, string)
print(x)
# x = ''.join(x)

# Exercício de CPF com regex
string = "058-471-753.94"
pattern =  re.compile(r'[\d]{3}\-[\d]{3}\-[\d]{3}\.[\d]{2}')

encontrar = re.findall(pattern, string)
print(encontrar)

# Exercício de Email com regex

string = "pedrow1@outmail.com"

pattern = re.compile(r'[\w]{4,15}\@[a-zA-Z]+mail\.com[\.[a-zA-Z]{0,5}]?')
find = re.fullmatch(pattern, string)
print(find)
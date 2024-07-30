import locale
from calendar import*

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
year = int(input("Entre com o ano: "))
print(calendar(year, 3, 1, 8, 3))

#3 = 3 caracteres para dias (seg, ter, qua)
#1 = 1 linha por semana
#8 = 8 linhas por mes
#3 = 3 colunas para todos os meses do ano
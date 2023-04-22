# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

# from pytz import timezone

data = datetime.now()
print(data.timestamp())  # Isso está na base de dados
print(datetime.fromtimestamp(1679269892))
# data_str = '2023-03-19 20:27:8'
# data_str = '19/03/2023'
# data_formato = '%d/%m/%Y'

# # data = datetime(2023, 3, 19, 20, 27, 8)
# data = datetime.strptime(data_str, data_formato)

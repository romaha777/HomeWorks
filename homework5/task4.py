#!usr/bin/python3

# -*- coding: utf-8 -*import

logs=[
    "ERROR: Не удалось подключиться к базе данных",
    "INFO: Пользователь вошёл в систему",
    "WARNING: Низкая память",
    "ERROR: Ошибка аутентификации",
    "INFO: Отчёт сформирован"
]

LogsFormatted=[]
count=0
for log in logs:
    if log.startswith("ERROR"):
        count+=1
        LogFormatted=log.split(":", 1)[1].strip()
        LogsFormatted.append(LogFormatted)
print(f"""Найдено ошибок: {count}
Ошибки:
{LogsFormatted[0]}
{LogsFormatted[1]}""")
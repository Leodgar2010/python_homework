# Напишите программу, удаляющую
# из текста все слова, содержащие ""абв"".
text = open('5-1.txt', 'r', encoding='utf-8')
lst = list(text.read().split())
text.close()
print(lst)
result = list(filter(lambda x: "абв" not in x, lst))
print(result)

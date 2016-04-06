import re

while (True):
    try:
        x = str(raw_input(u"Введите предложение:\n"))
    except:
        print u"Ошибка!\n"
    else:
        break

result = re.findall(r'[A-Z][A-Za-z]*\d\d\b', x)
print result

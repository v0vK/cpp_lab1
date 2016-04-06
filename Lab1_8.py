while (True):
    try:
        x = str(raw_input(u"Введите предложение:\n"))
    except:
            print u"Ошибка!\n"
    else:
        break

x=x.split(' ')

y=(sorted(x,key=lambda a: -len(a)))
print y

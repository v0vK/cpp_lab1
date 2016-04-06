while (True):
    try:
        x = int(input(u"Введите число из 16 цифр:\n"))
        if x<0:
            raise NameError()
        x=str(x)
        if len(x)!=16:
            raise NameError()
    except:
            print u"Ошибка!\n"
    else:
        break

print x[0:4]+'*'*8+x[12:16]

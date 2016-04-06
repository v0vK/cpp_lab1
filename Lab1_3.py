while (True):
    try:
        enter = float(input(u"Введите положительное дробное число:\n"))
        if enter<0:
            raise NameError("negative")
    except NameError as inst:
        val=inst.args
        if (val[0]=="negative"):
            print u"Ошибка. Введено отрицательное число\n"
        else:
            print u"Ошибка. Введенные данные не являются дробным числом.\n"
    else:
        break

rub=str(int(enter//1))
kop=str(int(enter%1*100))

print rub+u" руб. "+kop+u" коп."

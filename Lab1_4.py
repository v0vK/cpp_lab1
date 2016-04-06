while (True):
    try:
        val = int(input(u"Введите точность расчета:\n"))
        if val<0:
            raise NameError("negative")
    except NameError as inst:
        val=inst.args
        print inst.message
        if (val[0]=="negative"):
            print u"Ошибка. Введено отрицательное число\n"
        else:
            print u"Ошибка. Введенные данные не является числом.\n"
    else:
        break

pi=0.0
znak=1
for i in range(1, val*2+1, 2):
    pi+=znak*1/float(i)
    znak*=-1
    
pi*=4
print "pi="+str(pi)

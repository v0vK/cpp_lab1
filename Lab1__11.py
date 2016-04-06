while (True):
    try:
        x=int(input(u"Введите натуральное число:\n"))
        if (x<0):
            print u"Ошибка! Число должно быть позитивным."
        else:
            break
    except Exception:
        print u"Ошибка! Введено не натуральное число."

flag = False
for i in range(0,int(x**(1.0/3.0))+1):
    for j in range(0,x-i**3):
        if (x-i**3-j**3)>0:
            if ((x-i**3-j**3)**(1.0/3.0))%1==0:
                k=(x-i**3-j**3)**(1.0/3.0)
                if i**3+j**3+k**3==x:
                    print str(i)+"^3+"+str(j)+"^3+"+str(int(k))+"^3="+str(x)
                    flag=True

if not flag:
    print "No such combinations!"

import os
import sys

if sys.platform=='win32':os.system('cls')
else:os.system('clear')

n = 0
while (True):
    try:
        inp = input(u"Введите возраст (1 до 100)\n")
        x = int(inp)
        if (x<=0 or x>100):
            if (x<0):
                if sys.platform=='win32':os.system('cls')
                else:os.system('clear')
                print u"Ошибка! Число должно быть позитивным"
            else:
                if sys.platform=='win32':os.system('cls')
                else:os.system('clear')
        else:
            break
    except Exception:
        if sys.platform=='win32':os.system('cls')
        else:os.system('clear')


if (x>10 and x<15):
    print str(x)+u" лет"
else:
    x=str(x)
    index=len(x)-1
    if (x[index]=='1'): print str(x)+u" год"
    if (int(x[index])>1 and int(x[index])<5): print str(x)+u" года"
    if (int(x[index])>4 and int(x[index])<9): print str(x)+u" лет"
    if (x[index]=='0'): print str(x)+u" лет"



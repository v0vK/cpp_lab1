while (True):
    try:
        x = str(raw_input(u"Введите предложение и завершите точкой:\n"))
        if x[len(x)-1]!='.':
            raise NameError
    except:
            print u"Ошибка!\n"
    else:
        break

y=list(filter(None,x[:len(x)-1:].replace(',', ' ').replace('-', ' ').split(' ')))
print y

itog=""

for w in range(0,len(y)):
    print y[w] + "("+str(w)+")"
    itog+=y[w] + "("+str(w)+")"

print itog

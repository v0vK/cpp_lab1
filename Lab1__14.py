while (True):
    try:
        x = str(raw_input(u"Введите предложение и завершите точкой:\n"))
        x.split('.')[1]
    except:
            print u"Ошибка!\n"
    else:
        break
    
x=x.split('.')[0]
d={}
for w in x:
    if d.has_key(w):
        d[w]+=1
    else:
        d[w]=1

for w in d:
    if d[w]==1:
        print w

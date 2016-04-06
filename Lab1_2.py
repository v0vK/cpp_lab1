while (True):
    try:
        day = int(input(u"Введите день:\n"))
        if (day<0):
            print u"Ошибка! Число должно быть позитивным"
            continue
        month = int(input(u"Введите месяц:\n"))
        if (month<0):
            print u"Ошибка! Число должно быть позитивным"
            continue
        year = int(input(u"Введите год:\n"))
        if (year<0):
            print u"Ошибка! Число должно быть позитивным"
        else:
            break     
    except Exception:
        ""

day=str(day)
month=str(month)
year=str(year)
if len(day)==1:
    d="0"
else:
    d=""
    
if len(month)==1:
    m="0"
else:
    m=""

if len(year)==1:
    y="0"
else:
    y=""

print d+day+"/"+m+month+"/"+y+year

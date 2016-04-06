adr = raw_input(u"Введите строку:\n")

if (adr.startswith("www")):
    adr="http://"+adr
    if (not adr.endswith(".com")):
        adr+=".com"
print adr
        


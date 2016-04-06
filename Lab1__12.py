for x in range(1,100000):
    Num=0
    for i in range(1,int(x**(1.0/3.0))+1):
        if Num>=3:
            break
        else:
            for j in range(1,int((x-i**3)**(1.0/3.0))+1):
                if Num>=3:
                    break
                if (x-i**3-j**3)>0 and ((x-i**3-j**3)**(1.0/3.0))%1==0:
                    k=(x-i**3-j**3)**(1.0/3.0)
                    if i**3+j**3+k**3==x:
                        Num+=1
    if Num>=3:
        print str(x)+";";

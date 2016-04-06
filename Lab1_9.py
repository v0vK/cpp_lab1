import random

maximum=1000
x=random.randrange(0, maximum)

mas=[random.randrange(0, 99) for i in range(x)]

i=0
while 2**(i)<x:
    i+=1

print "nearest n^2="+str(i)+" ("+str(2**i)+"), x="+str(x)
mas=mas.__add__([0 for i in range(2**i-x)])

print mas

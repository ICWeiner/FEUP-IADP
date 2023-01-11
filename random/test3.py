import math 

x = float(input("x:"))
y = float(input("y:"))

f = (3*y + math.sqrt(2*x*(y+10)) ) /(4*x + y)

print("f({:.2f}".format(x)+",{:.2f}".format(y)+") = {:.2f}".format(f))
x = int(input())
pos = 0
print("n:{x}")
for i in x:
    y = int(input)
    print("value({i}):{y}")
    if y>=0:
        pos+=1


print("% positive values = {:.1f}".format(pos/x))
print("% negative values = {:.1f}".format((x - pos)/x))
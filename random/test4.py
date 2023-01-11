n = int(input())

m = [0 for i in range(n*n)]

for i in range((n*n)):
    m[i] = int(input())

max=-1

for i in range((n*n) - 1):
    if ( abs(m[i] - m[i +1] ) > max ):
            max =  abs(m[i] - m[i + 1])
            #print(str(m[i]) + " - " + str(m[i + 1]) + " = " + str(abs(m[i] - m[i + 1])))

print(str(max))
import numpy

n = int(input("Number of rows ="))
m = int(input("Number of columns ="))

lista_1 = []


for i in range(n):
    a = []
    for j in range(m):
        a.append(input("a[" + str(i) + "," + str(j) + "]="))
    lista_1.append(a)


array1 = numpy.array(lista_1).astype('float64').transpose()

print("Matrix transpose:")


for line in array1:
    print(line)


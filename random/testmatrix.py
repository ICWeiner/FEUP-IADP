import numpy

n = int(input())
m = int(input())

lista_1 = []
lista_2 = []

for i in range(n):
    a = []
    line = input()
    line_int = line.split(",")
    for number in line_int:
        a.append(number)
    lista_1.append(a)

for i in range(n):
    a = []
    line = input()
    line_int = line.split(",")

    for number in line_int:
        a.append(number)
    lista_2.append(a)

array1 = numpy.array(lista_1).astype('float64')
array2 = numpy.array(lista_2).astype('float64')

final_array =numpy.add(array1,array2)

for line in final_array:
    print(line)


import csv
with open(input("Filename:"), 'r') as file:
    reader = csv.reader(file)
    column=input("Column name:")
    fun=input("Function name:")
    csvr = list(reader)

    index = -99
    for row in csvr[:1]:
        if column in row[0]:
            index = row[0].split(";").index(column)
    value = 0
    if fun == "max":
        max = -9999
        for row in csvr[1:]:
            if max < int(row[0].split(";")[index]):
                max = int(row[0].split(";")[index])
        value = max
    elif fun == "min":
        min = -9999
        for row in csvr[1:]:
            if min > int(row[0].split(";")[index]):
                min = int(row[0].split(";")[index])
        value = min
    else:
        sum = 0
        for row in csvr[1:]:
            sum += int(row[0].split(";")[index])
        value = sum


print(fun + "(" + column + ")={:.2f}".format(value))
#file = open((input("Filename:")))
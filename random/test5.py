f1 = open(input("Filename 1:"),"r")
f2 = open(input("Filename 2:"),"r")

names = set()

for line in f1:
    line = line.replace("\n","")
    names.add(line)

for line in f2:
    line = line.replace("\n","")
    names.add(line)

names_sorted = sorted(names)

for name in names_sorted:
    print(name)


#print(names_sorted)
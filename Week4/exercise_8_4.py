fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    bike = line.split()
    for word in bike:
        if word in lst: continue
        lst.append(word)
lst.sort()
print(lst)

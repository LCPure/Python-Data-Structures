name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
new_lst = []
for line in handle:
    if not line.startswith('From '): continue
    words = line.split()
    new_lst.append(words[1]) #populate new list with email sender and address
for word in new_lst:
    counts[word] = counts.get(word, 0) + 1

#print(counts)
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

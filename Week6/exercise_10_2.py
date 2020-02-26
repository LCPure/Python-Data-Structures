name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
new_lst = []

for line in handle:
    if not line.startswith('From '): continue # check for lines that start with 'From '
    words = line.split()
    hr_time = words[5] #get time component
    hour = hr_time.split(':') #split into hr:min:sec
    new_lst.append(hour[0]) #populate new list with hour and count

for word in new_lst: #check if word already in dictionary
    counts[word] = counts.get(word, 0) + 1

#print(counts)
time_lst = list() #setup temporary list
for word, count in list(counts.items()):
    time_lst.append((word,count)) #for tuple in list update temp list

time_lst.sort(reverse=False) #sort tuple by key in ascending order

for word, count in time_lst: #print out hour and counts
    print(word, count)

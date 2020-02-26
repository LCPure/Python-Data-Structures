# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    number_found = line.find('.')
    number_offset = 5
    number_string = line[number_found:number_found + number_offset]
    final_number = float(number_string)
    total = total + final_number
    count = count + 1

average = total/count
print('Average spam confidence:', average)

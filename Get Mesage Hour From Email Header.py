name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

time = []
counts = {}

for line in handle:
    if line.startswith("From "):
        words = line.split()
        time.append(words[5])
        
#list comprehension to split 
hours = [i.split(":") for i in time]

#count items within list
for item in hours:
    counts[item[0]] = counts.get(item[0], 0) + 1

#sort items and output them
for k,v in sorted(counts.items()):
    print(k,v)



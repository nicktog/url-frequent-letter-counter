import urllib

peat = list()
counts = dict()

url = raw_input('Enter url -')
fhand = urllib.urlopen(url)
print

for line in fhand:
   words = line.split()
   for word in words:
      counts[word] = counts.get(word,0) + 1
      
for k,v in counts.items():
    peat.append((v,k))
peat.sort(reverse=True)
for k,v in peat:
    if k > 1:
        print v,k
   
#print counts

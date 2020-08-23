import re

f = open('test.txt','r')
sentences = f.readlines()
#print(sentences)
numbers = []

for sentence in sentences:
    n = re.findall('[0-9]+', sentence)
    if len(n) > 0:
        numbers = numbers + n
sum = 0
for n in numbers:
    print(n)
    sum += int(n)

print(sum)







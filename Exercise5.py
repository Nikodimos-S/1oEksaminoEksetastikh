import re
import operator

with open('two_cities_ascii.txt') as f:
    mystring = f.read()

cleanString =re.sub('[^A-Za-z ]+', ' ', mystring)
cleanString=cleanString.upper()
cleanString=cleanString.split()
d = dict()#dictionary to count number of appearances of each word
for word in cleanString:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
wordcount=list(sorted_d.keys())
print("The top 10 most popular words are:")
for i in range(0,10):
    print(wordcount[i])#question a) answer

d.clear()
for word in cleanString:
    first_chars = word[0:2]
    if first_chars in d:
        d[first_chars] = d[first_chars] + 1
    else:
        d[first_chars] = 1

sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
wordcount=list(sorted_d.keys())
print("The top 3 most popular 2-letter combos are:")
for i in range(0,3):
    print(wordcount[i])#question b) answer

d.clear()
for word in cleanString:
    first_chars = word[0:3]
    if first_chars in d:
        d[first_chars] = d[first_chars] + 1
    else:
        d[first_chars] = 1

sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
wordcount=list(sorted_d.keys())
print("The top 3 most popular 3-letter combos are:")
for i in range(0,3):
    print(wordcount[i])#question c) answer
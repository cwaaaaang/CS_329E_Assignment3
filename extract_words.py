# extract_words.py

# imports
import re
import collections

# open all files to read or append
original = open("metamorphosis.txt", "r")
allwords = open("allwords.txt", "a")
uniqwords = open("uniquewords.txt", "a")
wordfreq = open("wordfrequency.txt", "a")

# all words to lowercase and remove all punctuation
for x in original:
    x = x.lower()
    x = re.sub(r'[^\w\s]','',x)
    allwords.write(x)
    
allwords.close()

allwords = open("allwords.txt", "r")

# create dictionary to store keys (words) and values (count)
uniq = {}

for x in allwords:
    line = x.split()
    for word in line:
        if word not in uniq:
            uniq[word] = 1
        else:
            uniq[word] += 1
            
# write the keys from the uniq dictionary to uniquewords.txt          
for k in uniq.keys():
    uniqwords.write(k + "\n")
    
uniqwords.close()

# tabulate the frequencies 
freq = {}
for v in uniq.values():
    if v not in freq:
        freq[v] = 1
    else:
        freq[v] += 1
        
# sort the frequencies from freq
od = collections.OrderedDict(sorted(freq.items()))

# write the sorted frequencies to wordfrequency.txt
for k, v in od.items():
    wordfreq.write(str(k) + ": " + str(v) + "\n")
    
wordfreq.close()
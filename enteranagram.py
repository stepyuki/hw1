import sys
import itertools
f = open("Search.txt","w")
print("Enter word")
ls = sys.stdin.readline()
word = sorted(''.join(ls.splitlines()))
anagram = []
for j in range(4,len(word)):
    for word_combi in itertools.combinations(word,j):
        anagram.append(''.join(word_combi))
anagram_set = sorted(set(anagram),key=anagram.index)
for word_write in anagram_set:
    f.write(word_write+"\n")
f.close()
        
        

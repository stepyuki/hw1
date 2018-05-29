import sys
ld = open("dict3.txt","r")
lines = ld.readlines()
ld.close()

print("Enter word")
ls = sys.stdin.readline()
word = sorted(''.join(ls.splitlines()))
searchword = ''.join(word)
print searchword
print("Search Result")
for line in lines:
    if line.find(searchword) >= 0:
        word = line[:-1].split(",")
        print word[1]

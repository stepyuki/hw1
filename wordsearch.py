import sys
ld = open("dict3.txt","r")
lines = ld.readlines()
ld.close()

print("Enter word")
ls = sys.stdin.readline()
searchword = ''.join(ls.splitlines())
for line in lines:
    if line.find(searchword) >= 0:
        word = line[:-1].split(",")
        print word[1]

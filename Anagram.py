f = open("test.txt","r")
wf = open("test2.txt","w")
wf2 = open("test3.txt","w")
#content = f.read()

for line in f:
    list = []
    for l in line:
        list.append(l.lower())
    list.sort()
    letter = ''.join(list)
    wf.writelines(letter)
    wf.write(line)

f.close()
wf.close()
with open("test2.txt")as wf:
    lines = wf.readlines()
    lines_sorted = sorted(lines)
    for l in lines_sorted:
        wf2.write(l)
wf.close()
wf2.close()

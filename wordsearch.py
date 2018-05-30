import sys
import itertools
import bisect
f = open("dict3.txt","r")
f2 = open("Search.txt","r")
lines = f.readlines()
search = f2.readlines()
f.close()
f2.close()
point_mvp = 0
word_mvp = []
print("Search Result")
for word in search:
    search_str = word.strip() + ","
    top_point = bisect.bisect_left(lines,search_str)
    end_point = bisect.bisect_left(lines,search_str[:-1]+chr(ord(search_str[-1])+1))
    result = lines[top_point:end_point]
    if len(result) != 0:
        result2 = result[0].split(",")
        point = 0
        for letter in result2[0]:
            if letter in ['c','f','h','l','m','p','v','w','y','q']:
                point += 2
            elif letter in ['j','k','x','z']:
                point += 3
            else:
                point += 1
        print(result2[1]+"--"+str(point))
        if point_mvp < point:
            point_mvp = point
            word_mvp = result2[1]
print("BEST:"+str(word_mvp))

#coding:utf-8
import sys
import itertools
import bisect
#辞書のファイル,1列目がアルファベット順,2列目はもとの単語
f = open("dict3.txt","r")
#検索する文字列の組み合わせ
f2 = open("Search.txt","r")
lines = f.readlines()
search = f2.readlines()
f.close()
f2.close()
point_mvp = 0
word_mvp = []
vowel_min = 0
print("Search Result")
#単語が存在しているか
for word in search:
    search_str = word.strip() + ","
    top_point = bisect.bisect_left(lines,search_str)
    end_point = bisect.bisect_left(lines,search_str[:-1]+chr(ord(search_str[-1])+1))
    result = lines[top_point:end_point]
    if len(result) != 0:
        result2 = result[0].split(",")
        point = 0
        vowel = 0
        #点数計算
        for letter in result2[0]:
            if letter in ['c','f','h','l','m','p','v','w','y','q']:
                point += 2
            elif letter in ['j','k','x','z']:
                point += 3
            else:
                point += 1
            #あまり母音を使わないようにする
            if letter in ['a','i','u','e','o']:
                vowel += 1
        print result2[1].strip(),
        if point_mvp < point or point_mvp == point and vowel_min > vowel:
            point_mvp = point
            word_mvp = result2[1]
            vowel_min = vowel
#一番良いものを出力
print("\nBEST:"+str(word_mvp))
print("POINT:"+str(point_mvp))

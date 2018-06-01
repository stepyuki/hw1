#coding:utf-8
#入力された文字列の組み合わせを列挙しファイルに書き込む
import sys
import itertools
import copy

print("Enter word")

word_dic = ["abc","abcc","acqu"]
#文字を入力
ls = sys.stdin.readline()
word_ent = sorted(''.join(ls.splitlines()))
anagram = []

for dic in word_dic:
    word_search = copy.deepcopy(word_ent)
    print("-----")
    print(word_search)
    print(dic)
    for i in range(0,len(dic)):
        if dic[i] in word_search:
            word_search.remove(dic[i])
            print(word_search)
            if i == len(dic)-1:
                print("OK:")
                print(dic)
        else:
            break


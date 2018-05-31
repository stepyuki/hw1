#coding:utf-8
#入力された文字列の組み合わせを列挙しファイルに書き込む
import sys
import itertools
f = open("Search.txt","w")
print("Enter word")

#文字を入力
ls = sys.stdin.readline()
word = sorted(''.join(ls.splitlines()))
anagram = []
#qをquにする
for letter in word:
    if letter == 'q':
        word.append("qu")
        word.remove("u")
        word.remove("q")

#組み合わせを出力
for j in range(1,len(word)):
    for word_combi in itertools.combinations(word,j):
        anagram.append(''.join(word_combi))
anagram_set = sorted(set(anagram),key=anagram.index)
for word_write in anagram_set:
    word_sep = sorted(list(word_write))
    f.write(''.join(word_sep)+"\n")
f.close()
        
        

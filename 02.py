"""【问题描述】

给定一个字符串，取出第一个没有重复的字符，如果输入为空则输出"None"。

【输入形式】

从标准输入得到一串字符串，可以为空

【输出形式】

第一个没有重复的字符，如果输入为空则输出"None"

【样例输入】

helloworldhahaha!

【样例输出】

e

【样例说明】

e和w都没有重复，但是e是第一个出现的，所以输出e"""
text = input()
dic1 = {}
time = 0
if text == '':
    print('None')
    exit()
for i in text:
    if i in text:
        dic1[i] = (dic1.get(i, (0, None))[0] + 1, time)
        time += 1
a = sorted(dic1.items(), key = lambda x:x[1][1])
a = sorted(dic1.items(), key = lambda x:x[1])
print(a[0][0])
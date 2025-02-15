"""    本题目要求读入一个字符串，输出字符串的最长数字子串。

【输入形式】

    输入一个字符串
【输出形式】

    输出最长数字子串，若有多个最长数字子串输出最后一个，若字符串无数字字符，则输出“No digits”。

【输入样例】

sdffsd123werrer456fgdgdg1dfgdf12

【样例输出】

  456 
【样例说明】"""
a = input()
b = ''
c = ''
for i in a:
    if i.isdigit():
        b += i
    else:
        if len(b) >= len(c):
            c = b
        b = ''
if len(b) >= len(c):
    c = b
if c == '':
    print('No digits')
else:
    print(c)

"""【问题描述】

    所谓“变位词”是指两个词之间存在组成字母的重新排列关系。如：heart和earth，python和typhon，1234与2134。

编程实现对输入的两个字符串判断是否为“变位词”，是输出True，不是输出False。

【输入形式】

输入两个字符串，一行一个字符串
【输出形式】

输出逻辑True或False
【样例输入】

heart

earth
【样例输出】

True
【样例说明】

11234与2134不是“变位词”
【评分标准】"""
a = input()
b = input()
if sorted(a) == sorted(b):
    print(True)
else:
    print(False)
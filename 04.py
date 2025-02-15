"""【问题描述】   

    编写程序，对输入的密码（长度不超过28）进行强度检测。密码强度规定为：

    1）含有数字字符；

    2)含有小写字母； 

    3）含有大写字母；

    4）密码长度不低于8；

    5）至少含有~!@#$%^&*()_=-/,.?<>;:[]{}|\中的一个字符

    规定密码满足上列任意条件即加一星，程序输出密码的星级

【输入形式】

  长度在28以内的任意字符串。

【输出形式】

    根据密码强度要求，输出密码强度星级，用整数表示

【样例输入】

123.aq.Aw!

【样例输出】

5

【评分标准】"""
a = input()
star = [0,0,0,0,0]
for i in a:
    if i.isdigit() and star[0] == 0:
        star[0] = 1
    if i.islower() and star[1] == 0:
        star[1] = 1
    if i.isupper() and star[2] == 0:
        star[2] = 1
    if i in "~!@#$%^&*()_=-/,.?<>;:[]{,}|\\" and star[3] == 0:
        star[3] = 1
    if len(a) >= 8 and star[4] == 0:
        star[4] = 1
totole = sum(star)
print(totole)

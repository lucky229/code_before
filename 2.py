#! usr/bin/env python3
# -*- coding:utf-8 -*-

n_renshu = input(' 请输入人数：')
l_one = list(range(1, int(n_renshu)+1))
s_times = []
i = 1

while True:
    print('请输入第%d次转身的倍数(输入0结束)：' % i)
    s1 = int(input())
    if s1 > 0 :
        s_times.append(s1)
        i = i + 1
    elif s1 == 0:
        break
    elif s1 < 0 :
        print('输入错误，请重新输入！')

for s in s_times:
    n1 = len(l_one)
    for n in range(n1):
        if l_one[n]%s == 0:
            l_one[n] = l_one[n] * (-1)

l_two = []
for n in range(len(l_one)):
    if l_one[n] > 0:
        l_two.append(l_one[n])

print('有%d个小朋友面对老师，经过%d轮转身后：' % (int(n_renshu), len(s_times)))
print('面对老师的学生数量为：%d' % len(l_two))
print('面对老师的同学有：', l_two)
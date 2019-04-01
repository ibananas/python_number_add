# -*- coding: utf-8 -*-
# @Time     : 2019/04/01 17:00
# @Author   : 刘洪波
# @Filename : 默认.py
# @Software : PyCharm
import random
import time


class num_add(object):
    def add1(self,a,b):  # 第一种方法，由于python3具有无限精度的int类型，所以大数可以直接运算
        startTime = time.time()
        c=int(a)+int(b)
        totalTime=time.time()-startTime
        print(c)
        print('方法一耗时{0}ms'.format(totalTime))
        return c,totalTime


    def add2(self,L1,L2):  #第二种方法

        startTime=time.time()
        #长度强行扭转到一致 不够前面补0
        max_len= len(L1) if len(L1)>len(L2) else len(L2)
        l1=L1.zfill(max_len)
        l2=L2.zfill(max_len)

        a1=list(l1)
        a2=list(l2)
        #长度一致 每个对应的位置的相加的和 %10 前一位补1 如果>10 否则0  99+99最大3位所以多一位
        a3=[0]*(max_len+1)

        for index in range(max_len-1,-1,-1):
            index_sum=a3[index+1]+int(a1[index])+int(a2[index])
            less=index_sum-10
            a3[index+1]=index_sum%10
            a3[index]=1 if less>=0 else 0
        if(a3[0]==0):
            a3.pop(0)
        a33=[str(i) for i in a3]
        a44=''.join(a33)
        totalTime = time.time() - startTime
        print(a44)
        print('方法二耗时{0}ms'.format(totalTime))
        return a44,totalTime



class tool(object):
    def random_number(self,digits):   # 生成任意长度的大数
        number=[]
        number = "".join([str(random.randint(0, 9)) for i in range(0, digits)])
        return number

    def are_equal(self,j,k):  # 验证两种方法相加后的结果是否相等
        if int(j) == int(k):
            print("两数相等")
        else:
            print("两数不相等")
    def time_faster(self,t1,t2):# 验证两种方法那种比较快
        if t1 > t2:
            print("方法二速度较快")
        else:
            print("方法一速度较快")


# u=tool()
# num1=u.random_number(90000)    #在90000位数时两种方法时间大致相等，大于90000位数时方法二较快，小于90000位数时方法一较快
# num2=u.random_number(90000)
# print(num1)
# print(num2)
# s=num_add()
# j,t1=s.add1(num1,num2)
# k,t2=s.add2(num1,num2)
# 
# u.are_equal(j,k)
#
# u.time_faster(t1,t2)
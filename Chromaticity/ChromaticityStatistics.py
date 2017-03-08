"""
Author: CIEL
Date: 2017.02.27
Function:  统计色度差分每个像素的CD值
"""
from functools import reduce  #从 functools 包里调用 reduce 
import matplotlib.pyplot as plt
import numpy as np
import sys
import math
    

#自定义函数str2float():将字符串转换成浮点数
#注：该函数只能转化正数，不能转化负数
def str2float(s):
    def fn(x,y):  #定义一个 fn() 函数，用来把S1，S2这两个list里面的元素变成一个数。 
        return x*10+y
    n=s.index('.')  #利用 index() 函数确定字符串S中'.'的位置
    '''
    先利用切片把我们传入的 str 分成以前以后两个部分（其实就是根据小数点分成整数和浮点数，分别处理），
    然后再把切割好的 str 利用 int 变成整数，
    map() 函数负责把 int 作用到截取的 str 的每个元素中去
    map()函数要接收两个参数，第一个参数为函数，第二个参数为一个Iterable对象，map将传入的函数依次作用到序列的每个元素，结果以Iterable返回
    reduce()函数也接收两个参数，与map一样，但是reduce函数是把结果和序列中剩下的元素一起继续参与运算
    '''
    s1=list(map(int,[x for x in s[:n]]))
    s2=list(map(int,[x for x in s[n+1:]]))
    return reduce(fn,s1)+reduce(fn,s2)/10**len(s2)   #m**n 这个表达的就是 m 的 n 次方
#print('\'123.4567\'=',str2float('123.4567'))

#横坐标：CD范围
xticks=['-0.2','-0.19','-0.18','-0.17','-0.16','-0.15','-0.14','-0.13','-0.12','-0.11','-0.1','-0.09','-0.08','-0.07','-0.06','-0.05','-0.04','-0.03','-0.02','-0.01','0','0.01','0.02','0.03','0.04','0.05','0.06','0.07','0.08','0.09','0.1','0.11','0.12','0.13','0.14','0.15','0.16','0.17','0.18','0.19','0.2']
#纵坐标：符合区间的频数统计
yticks=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
#以下：将txt文件中的数据，保存到中
cd_B=[] #保存cd_B中的数据
with open('E:\\CIEL\\中科院的七七八八\\NSSC\\CODE\\Statistics Histogram\\Chromaticity\\cd_B.txt', 'r') as f:  
    data = f.readlines()  #txt中所有字符串读入data  
  
    for line in data:  
        row = line.split()        #将单个数据分隔开存好
        length=len(row)
        #print(length)
        #print(row)
        for x in row:
            if '-1.#IND' not in x:  #如果x！='-1.#IND'
                temp=float(x)  #将字符串强制转换为浮点型
                #print(temp)  #到此，已成功转换
                cd_B.append(temp)  #将有效数据保存到cd_B中

#遍历数组
for i in range(0,len(cd_B)):
    #print (i,cd_B[i])
    if cd_B[i]>=-0.204 and cd_B[i]<=-0.196 :  #x=-0.2
        yticks[0]=yticks[0]+1
    if cd_B[i]>=-0.194 and cd_B[i]<=-0.185 :  #x=-0.19
        yticks[1]=yticks[1]+1
    if cd_B[i]>=-0.184 and cd_B[i]<=-0.175 :  #x=-0.18
        yticks[2]=yticks[2]+1
    if cd_B[i]>=-0.174 and cd_B[i]<=-0.165 :  #x=-0.17
        yticks[3]=yticks[3]+1
    if cd_B[i]>=-0.164 and cd_B[i]<=-0.155 :  #x=-0.16
        yticks[4]=yticks[4]+1
    if cd_B[i]>=-0.154 and cd_B[i]<=-0.145 :  #x=-0.15
        yticks[5]=yticks[5]+1
    if cd_B[i]>=-0.144 and cd_B[i]<=-0.135 :  #x=-0.14
        yticks[6]=yticks[6]+1
    if cd_B[i]>=-0.134 and cd_B[i]<=-0.125 :  #x=-0.13
        yticks[7]=yticks[7]+1
    if cd_B[i]>=-0.124 and cd_B[i]<=-0.115 :  #x=-0.12
        yticks[8]=yticks[8]+1
    if cd_B[i]>=-0.114 and cd_B[i]<=-0.105 :  #x=-0.11
        yticks[9]=yticks[9]+1
    if cd_B[i]>=-0.104 and cd_B[i]<=-0.095 :  #x=-0.1
        yticks[10]=yticks[10]+1
    if cd_B[i]>=-0.094 and cd_B[i]<=-0.085 :  #x=-0.09
        yticks[11]=yticks[11]+1
    if cd_B[i]>=-0.084 and cd_B[i]<=-0.075 :  #x=-0.08
        yticks[12]=yticks[12]+1
    if cd_B[i]>=-0.074 and cd_B[i]<=-0.065 :  #x=-0.07
        yticks[13]=yticks[13]+1
    if cd_B[i]>=-0.064 and cd_B[i]<=-0.055 :  #x=-0.06
        yticks[14]=yticks[14]+1
    if cd_B[i]>=-0.054 and cd_B[i]<=-0.045 :  #x=-0.05
        yticks[15]=yticks[15]+1
    if cd_B[i]>=-0.044 and cd_B[i]<=-0.035 :  #x=-0.04
        yticks[16]=yticks[16]+1
    if cd_B[i]>=-0.034 and cd_B[i]<=-0.025 :  #x=-0.03
        yticks[17]=yticks[17]+1
    if cd_B[i]>=-0.024 and cd_B[i]<=-0.015 :  #x=-0.02
        yticks[18]=yticks[18]+1
    if cd_B[i]>=-0.014 and cd_B[i]<=-0.005 :  #x=-0.01
        yticks[19]=yticks[19]+1
    if cd_B[i]>=-0.004 and cd_B[i]<=0.004 :  #x=0
        yticks[20]=yticks[20]+1
    if cd_B[i]>=0.005 and cd_B[i]<=0.014 :  #x=0.01
        yticks[21]=yticks[21]+1
    if cd_B[i]>=0.015 and cd_B[i]<=0.024 :  #x=0.02
        yticks[22]=yticks[22]+1
    if cd_B[i]>=0.025 and cd_B[i]<=0.034 :  #x=0.03
        yticks[23]=yticks[23]+1
    if cd_B[i]>=0.035 and cd_B[i]<=0.044 :  #x=0.04
        yticks[24]=yticks[24]+1
    if cd_B[i]>=0.045 and cd_B[i]<=0.054 :  #x=0.05
        yticks[25]=yticks[25]+1
    if cd_B[i]>=0.055 and cd_B[i]<=0.064 :  #x=0.06
        yticks[26]=yticks[26]+1
    if cd_B[i]>=0.065 and cd_B[i]<=0.074 :  #x=0.07
        yticks[27]=yticks[27]+1
    if cd_B[i]>=0.075 and cd_B[i]<=0.084 :  #x=0.08
        yticks[28]=yticks[28]+1
    if cd_B[i]>=0.085 and cd_B[i]<=0.094 :  #x=0.09
        yticks[29]=yticks[29]+1
    if cd_B[i]>=0.095 and cd_B[i]<=0.104 :  #x=0.1
        yticks[30]=yticks[30]+1
    if cd_B[i]>=0.105 and cd_B[i]<=0.114 :  #x=0.11
        yticks[31]=yticks[31]+1
    if cd_B[i]>=0.115 and cd_B[i]<=0.124 :  #x=0.12
        yticks[32]=yticks[32]+1
    if cd_B[i]>=0.125 and cd_B[i]<=0.134 :  #x=0.13
        yticks[33]=yticks[33]+1
    if cd_B[i]>=0.135 and cd_B[i]<=0.144 :  #x=0.14
        yticks[34]=yticks[34]+1
    if cd_B[i]>=0.145 and cd_B[i]<=0.154 :  #x=0.15
        yticks[35]=yticks[35]+1
    if cd_B[i]>=0.155 and cd_B[i]<=0.164 :  #x=0.16
        yticks[36]=yticks[36]+1
    if cd_B[i]>=0.165 and cd_B[i]<=0.174 :  #x=0.17
        yticks[37]=yticks[37]+1
    if cd_B[i]>=0.175 and cd_B[i]<=0.184 :  #x=0.18
        yticks[38]=yticks[38]+1
    if cd_B[i]>=0.185 and cd_B[i]<=0.194 :  #x=0.19
        yticks[39]=yticks[39]+1
    if cd_B[i]>=0.195 and cd_B[i]<=0.204 :  #x=0.2
        yticks[40]=yticks[40]+1

N=41  #x轴共41个坐标
ind=range(N)
width=0.5 #柱的宽度

#创建柱状图
'''
bar(left, height, width, color, align, yerr)函数：绘制柱形图。
left为x轴的位置序列，一般采用arange函数产生一个序列；
height为y轴的数值序列，也就是柱形图的高度，一般就是我们需要展示的数据；
width为柱形图的宽度，一般这是为1即可；
color为柱形图填充的颜色;
align设置plt.xticks()函数中的标签的位置；
yerr让柱形图的顶端空出一部分。
'''
plt.bar(ind, yticks, width, color='blue', align='center', yerr=0.0001)

#设置柱的说明文字
#第一个参数为文字说明的横坐标，第二个参数为文字说明内容
plt.xticks(ind, xticks)

#添加图形属性
plt.xlabel('CD in channel B')  #设置横坐标的文字说明
plt.ylabel('Number of Pixel')   #设置纵坐标的文字说明
plt.title('CD Statistics in Channel B')  #设置标题

#绘图
plt.show()

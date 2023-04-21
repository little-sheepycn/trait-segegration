'''
    该程序会在执行目录下生成result.txt,请使用文本编辑器的查找功能进行统计，注意该程序区分了d D与D d，请将这两组的数据相加
'''

import random
trait=['D','d']
numbers=int(input())
f=open('./result.txt','w+')
for i in range(1,numbers):
    print(trait[random.randint(0,1)],trait[random.randint(0,1)],end=',',file=f)

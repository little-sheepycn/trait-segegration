import random
trait=['D','d']
result={'DD':0,'dd':0,'Dd':0}
numbers=int(input('请输入豌豆数量:'))
with open('./result.txt','w+') as file:
    for i in range(numbers):
        trait1=random.choice(trait)
        trait2=random.choice(trait)
        gene=trait1+trait2
        if gene =='DD':
            result['DD']+=1
            print('D','D',end='',file=file)
            print(',',end='',file=file)
        elif gene =='dd':
            result['dd']+=1
            print('d','d',end='',file=file)
            print(',',end='',file=file)
        else:
            result['Dd']+=1
            print('D','d',end='',file=file)
            print(',',end='',file=file)
print('结果：')
for key,value in result.items():
    print(key,':',value)

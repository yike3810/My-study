# coding:utf8
import time

starttime=time.time()
f = open('xyj.txt','r',encoding="utf8")

sumstr = 0
characers = []
stat={}
for line in f:
    line = line.strip()
    if len(line) ==0:
        continue
    # print(line)

    for x in range(0,len(line)):
        if line[x] in [ ',','\n','\t','\r','，','。','！','·','~','@','#','￥','%','%','…','&','*','（','）','-','+','_','=','【','】','{','}','《','》','、','？','：','；','”','“','’','‘',',','.','/','?','>','<',':',';','"','\'','=','-',')','(','*']:
            continue
        sumstr+=1
        if not line[x] in characers:
            characers.append(line[x])
        if not line[x] in stat:
            stat[line[x]]=0
        stat[line[x]] += 1
# 输出字典
# for key,value in stat.items():
#     print(key,value)

#print(len(stat))
# print(len(characers))

stat = sorted(stat.items(),key=lambda d:d[1],reverse=True)

print('*'*20+' 西游记 字数统计 '+'*'*20)

print('总字数：%s  共出现了%s个不同的汉字'%(sumstr,len(stat)))
print('出现频次由低到高排列如下：')
for x in range(0 ,len(stat)):
    print('第 %s 名： %s  出现次数： %s'%(x+1,stat[x][0],stat[x][1]))

f.close()
endtime=time.time()
tm=endtime-starttime

print(tm)
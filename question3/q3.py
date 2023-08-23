import gettime
results={}
timepoints={}
n=int(input())
m,t=map(int,input().split())
try:
    while True:
        timepoint,address,result=map(str,input().split(","))
        if address not in results.keys():
           results[address]=[result]
           timepoints[address]=[timepoint]
        else:
            results[address].append(result)
            timepoints[address].append(timepoint)
except EOFError:
        pass
for e in results.keys():
    if "-" in results[e]:
        i=0
        start=0
        err=False
        while i<len(results[e]):
            if err==False and results[e][i:i+n]==["-"]*n:
                start=i
                err=True
            elif err==True and results[e][i]!="-":
                err=False
                print(e,"was under error for",gettime.gettime(timepoints[e][i],results[e][i])-gettime.gettime(timepoints[e][start],0),"since",gettime.gettime(timepoints[e][start],0))
            if i==len(results[e])-1 and err:
                print(e,"under error since",gettime.gettime(timepoints[e][start],0))
                break
            i+=1
    if len(results[e])>=m:
        for i in range(m-1,len(results[e])):
            s=0
            for j in range(1+i-m,i+1):
                if results[e][j]=="-":
                    s+=1000
                else:
                    s+=int(results[e][j])
            if s>m*t:
                print(e,"overflows for",gettime.gettime(timepoints[e][i],results[e][i])-gettime.gettime(timepoints[e][i-m+1],0),"since",gettime.gettime(timepoints[e][i-m+1],0))
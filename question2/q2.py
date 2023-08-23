import gettime
results={}
timepoints={}
n=int(input())
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

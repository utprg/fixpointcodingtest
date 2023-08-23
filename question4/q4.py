from ipaddress import ip_network
import gettime
results={}
timepoints={}
errorperiods={}
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
        errorperiods[e]=[]
        i=0
        start=0
        err=False
        while i<len(results[e]):
            if err==False and results[e][i:i+n]==["-"]*n:
                start=i
                err=True
            elif err==True and results[e][i]!="-":
                err=False
                print(e,gettime.gettime(timepoints[e][i],results[e][i])-gettime.gettime(timepoints[e][start],0),"since",gettime.gettime(timepoints[e][start],0))
                errorperiods[e].append((gettime.gettime(timepoints[e][start],0),gettime.gettime(timepoints[e][i],results[e][i])))
            if i==len(results[e])-1 and err:
                print(e,"under error since",gettime.gettime(timepoints[e][start],0))
                errorperiods[e].append((gettime.gettime(timepoints[e][start],0),gettime.gettime("99991231235959","999")))
                break
            i+=1
for i in range(len(errorperiods.keys())-1):
    for j in range(i+1,len(errorperiods.keys())):
        ip1=ip_network(errorperiods.keys()[i])
        ip2=ip_network(errorperiods.keys()[j])
        
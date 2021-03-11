#given an array of starting positions of different people [a0,b0,c0..] and their speeds(constant) [a',b',c'...]
#they all start running at the same time and can run forever.
#find the maximum number of people at some intersection. If no intersection then return -1. 

def runnersMeetings(sp, speed):
    maxx = []
    for i in range(len(sp)):
        
        times = []
        for j in range(i+1,len(sp)):
            if speed[j] != speed[i] and (sp[i]-sp[j])/(speed[j]-speed[i])>0:
                times.append((sp[i]-sp[j])/(speed[j]-speed[i]))
        
        if len(times)>0: maxx.append(1+times.count(max(times,key=times.count)))
    
    return max(maxx) if len(maxx)>0 else -1
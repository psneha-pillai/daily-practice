def aggressivecows(stalls,k):
    def conweplace(mindist,stalls,k):
        cow=stalls[0]
        placedcows=1
        for stall in range(1,len(stalls)):
            if(stalls[stall]-cow>=mindist):
                cow=stalls[stall]
                placedcows+=1
            if(placedcows>=k):
                return True
            if(placedcows<k):
                return False
        stalls.sort()
        Min=min(stalls)
        Max=max(satalls)
        if(k==2):
            return Min-max
        for mindist in range(1,Min-Max+1):
            if(canweplace(mindist,stall,k)):
                continue
            else:
                return mindist-1
stalls=list(map(int,input().split()))
k=int(input())
print(aggressivecows(stalls,k))
            

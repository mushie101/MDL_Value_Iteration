import numpy as np
actions=['shoot','dodge','recharge']
x=48
y=-20
aa=[]
bb=[]
cc=[]
act1=np.zeros((60,60))     #created 60*60 matrix for transiiton probability function
act3=np.zeros((60,60))
act2=np.zeros((60,60))
def shoot_transition():
    h=5
    a=4
    s=3
    for i in range(h):
        for j in range(a):
            for k in range(s):
                me=(i,j,k)
                calc=np.asarray(me)
                aa.append(calc)
    #aa=aa.reshape(1,60)
    #for i in range(60):
    print(np.shape(aa))  #totally have 60 rows in which , each row has array with three elements
    #print(np.shape(me))   #printing it's dimensions
    for ii in range(12,60,1):
        for jj in range(60):
            #below statement is for printing and checking values in 60*60 matrix if they are having correct comparision
            #print(aa[ii][0],aa[ii][1],aa[ii][2],aa[jj][0],aa[jj][1],aa[jj][2])
            #condition when arrows or stamina or health increases which can actuallly never happen , so zero
            #if((aa[ii][2]-aa[jj][2])==1 or (aa[ii][1]-aa[jj][1])==1 or aa[ii][0]<aa[jj][0]):
            #act1[ii][jj]=0
            #condition when health got reduced and even arrow which means hit MD with arrow with probabitlity 0.5
            if((aa[ii][0]-aa[jj][0])==1 and (aa[ii][1]-aa[jj][1])==1 and (aa[ii][2]-aa[jj][2])==1):
                act1[ii][jj]=0.5
            #condition when hit with arrow but didn't touch
            if((aa[ii][0]-aa[jj][0])==0 and (aa[ii][1]-aa[jj][1])==1 and (aa[ii][2]-aa[jj][2])==1):
               act1[ii][jj]=0.5
            if(aa[ii][1]==0 or aa[ii][2]==0):
                act1[ii][ii]=1
    count=0
    for i in range(0,60,1):
        for j in range(0,60,1):
            if(act1[i][j]!=0):
                count=count+1
    print(count)            

def recharge_transition():
    h=5
    a=4
    s=3
    for i in range(h):
        for j in range(a):
            for k in range(s):
                me=(i,j,k)
                calc=np.asarray(me)
                bb.append(calc)
    #print(np.shape(bb))
    for l in range(12,60,1):
        for m in range(60):
            #below condition checks if stamina is increased by 50 points which means 1 , so it is with probability 0.8 as given
            if((bb[m][2]-bb[l][2])==1):
                act3[l][m]=0.8
            #below condition checks if stamina is not increased by 50 points which means 1 , so it is with probability 0.2 as given
            if((bb[m][2]-bb[l][2])==0):
                act3[l][m]=0.2

def dodge_transition():
    h=5
    a=4
    s=3
    for i in range(h):
        for j in range(a):
            for k in range(s):
                me=(i,j,k)
                calc=np.asarray(me)
                cc.append(calc)
    #print(np.shape(bb))
    for u in range(12,60,1):
        for v in range(60):
            #below condition if he has stamina 100 points at first (which means 2) 
            if(cc[u][2]==2):
                #below condition if stamina reduces from 100 to 50 then probability is 0.8
                if((cc[u][2]-cc[v][2])==1):
                    act2[u][v]=0.8
                #below condition if stamina reduces from 100 to 0 then probability is 0.2
                if((cc[u][2]-cc[v][2])==2):
                    act2[u][v]=0.2
            #below condition if he has stamina 50 points at first (which means 1) 
            if(cc[u][2]==1):
                #below condition when stamina drops down to 0 from 50 then probability is 1
                if((cc[u][2]-cc[v][2])==1):
                    act2[u][v]=1
            #below condition if he picks an arrow , 
            if((cc[u][2]-cc[v][2])==1):
                act2[u][v]=0.8
            #below condition if he doesn't pick an arrow    
            if((cc[u][2]-cc[v][2])==0):
                act2[u][v]=0.2

def maximum(a, b, c): 
  
    if (a >= b) and (a >= b): 
        largest = a 
  
    elif (b >= a) and (b >= a): 
        largest = b 
    else: 
        largest = c 
          
    return largest 


shoot_transition()
dodge_transition()
recharge_transition()

#creating utility function , for every state so 60*1 matrix
current_util=np.zeros((60,1))

#creating previous utility function, for every state so 60*1 matrix
prev_util=np.zeros((60,1))

#print(prev_util)


for i in range(12,60,1):
    #storing current actions with shoot , dodge, recharge
    current_action=np.zeros((3,1))
    #print(current_action)
    #print(np.shape(current_action))
    a=0
    b=0
    c=0
    for j in range(60):
        #print(current_action)
        #modifying action values according to transition functions
        a+=act1[j][j]+current_util[i]  #for shoot action

        b+=act2[i][j]+current_util[i]  #for dodge action

        c+=act3[i][j]+current_util[i]  #for recharge action

        maxh=maximum(a,b,c)
        print(maxh,"he")

        prev_util=current_util[i]
        current_util[i]=y+0.99*maxh

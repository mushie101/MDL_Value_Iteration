import numpy as np
actions=['shoot','dodge','recharge']
x=48
y=-20

class Implement():
    def __init__(self):
        self.arrows=3
        self.current_arrows=3
        self.max_lero_stamina=100
        self.stamina=100
        self.stamina_value=2   #(0,50,100) mapped to (0,1,2)
        self.max_MD_health=100
        self.health_value=4   #(0,25,50,75,100) mapped to (0,1,2,3,4)
        self.health=100
        self.penalty=-20
        self.gamma=0.99
        self.delta=0.001
        self.reward=100
        self.over_health=0
        self.utility = [[0 for i in range(3)]for j in range(3)]


    def happy_ending(self):
        self.net_reward += self.final_reward
        self.end_game = True
    
    def Shoot(self):
        self.hit_probability = 0.5
        if self.current_ammo >= 1:
            self.current_ammo -= 1
            self.stamina -= 50
            self.stamina_value -=1
            if self.hit == True:
                self.md_health -= 25
                self.health_value -= 1
        if self.stamina == 0 or self.ammo == 0:
            self.shoot = False
    
    def Recharge(self):
        self.recharge_probability = 0.8
        if self.recharge == True:
            self.stamina += 50
            self.stamina_value += 1
            if self.stamina > 100: self.stamina = 100

    def Dodge(self):
        self.dodge_probability = 0.8 
        self.arrow_pick_probability = 0.8
        if self.dodge == True():
            if self.stamina==100:
                self.stamina -= 50 
                self.stamina_value -=1  #with probability 0.8
            if self.stamina==50:
                self.stamina = 0  
                self.stamina_value =0 #with probability 1
            #if self.ammo < 3:  self.ammo += 1
    '''
    def value_iteration():
            count=0
            while(1):
                print("Iteration number ",count)
                for i in range(3):
                    min_val=0
                    for l in actions:
                        if l=="shoot":

                        if l=="recharge":

                        if l=="dodge":

                count++
    '''

    def shoot_transition(self):
        self.aa=[]
        self.h=5
        self.a=4
        self.s=3
        for i in range(self.h):
            for j in range(self.a):
                for k in range(self.s):
                    self.me=(i,j,k)
                    self.calc=np.asarray(self.me)
                    self.aa.append(self.calc)
        #self.aa=self.aa.reshape(1,60)
        #for i in range(60):
        print(np.shape(self.aa))  #totally have 60 rows in which , each row has array with three elements
        me=np.zeros((60,60))     #created 60*60 matrix for transiiton probability function
        print(np.shape(me))   #printing it's dimensions
        for ii in range(60):
            for jj in range(60):
                #condition when arrows or stamina or health increases which can actuallly never happen , so zero
                if(self.aa[ii][2]<self.aa[jj][2] or self.aa[ii][1]<self.aa[jj][1] or self.aa[ii][0]<self.aa[jj][0]):
                    me[ii][jj]=0
                #condition when health got reduced and even arrow which means hit MD with arrow with probabitlity 0.5
                if((self.aa[ii][0]-self.aa[jj][0])==1 and (self.aa[ii][1]-self.aa[jj][1])==1):
                    me[ii][jj]=0.5
                #condition when hit with arrow but didn't touch
                if((self.aa[ii][0]-self.aa[jj][0])==0 and (self.aa[ii][1]-self.aa[jj][1])==1):
                    me[ii][jj]=0.5





if __name__=='__main__':
    final=Implement()
    final.shoot_transition()

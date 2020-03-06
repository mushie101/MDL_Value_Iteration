import numpy as np
actions=['shoot','dodge','recharge']

class Implement():
    def __init__(self):
        self.arrows=3
        self.max_lero_stamina=100
        self.max_MD_health=100
        self.penalty=-20
        self.gamma=0.99
        self.delta=0.001
        self.reward=100
        self.utility = [[0 for i in range(3)]for j in range(3)]


    def happy_ending(self):
        self.net_reward += self.final_reward
        self.end_game = True
    
    def Shoot(self):
        self.hit_probability = 0.5
        if self.current_ammo >= 1:
            self.current_ammo -= 1
            self.stamina -= 50
            if self.hit == True:
                self.md_health -= 25
        if self.stamina == 0 or self.ammo == 0:
            self.shoot = False
    
    def Recharge(self):
        self.recharge_probability = 0.8
        if self.recharge == True:
            self.stamina += 50
            if self.stamina > 100: self.stamina = 100

    def Dodge(self):
        self.dodge_probability = 0.8 
        self.arrow_pick_probability = 0.8
        if self.dodge == True():
            self.stamina -= 50
            if self.ammo < 3:  self.ammo += 1

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



if __name__=='__main__':
    res=''
    main()

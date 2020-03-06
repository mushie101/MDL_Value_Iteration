import numpy as np


class Implement():
    def __init__(self):
        self.arrows=3
        self.actions=['shoot','dodge','recharge']
        self.max_lero_stamina=100
        self.max_MD_health=100
        self.penalty=-20
        self.gamma=0.99
        self.delta=0.001
        self.reward=100


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
    V=np.zeroes()

def update_q(self, state, action, reward, new_state):
        self.Q_table[state][action] += self.lr * (reward + self.discount * np.max(self.Q_table[new_state]) - self.Q_table[state][action])




if __name__=='__main__':
    res=''
    main()

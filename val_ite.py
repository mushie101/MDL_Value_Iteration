import numpy as np

class MD_saga_part_1():
    def __init__(self):
        self.x = 48
        self.y = -20
        self.max_ammo = 3
        self.current_ammo = 3
        self.health_val = 4
        self.stamina_val = 2
        self.final_reward = +10
        self.net_reward = 0
        self.actions = ['shoot', 'dodge', 'recharge']
        self.hit = True
        self.recharge = True
        self.dodge = True
        self.end_game = False

    def happy_ending(self):
        self.net_reward += self.final_reward
        self.end_game = True
    
    def Shoot(self):
        self.hit_probability = 0.5
        self.shoot_cost = -2.5
        if self.current_ammo >= 1 and self.stamina_val >= 1:
            self.current_ammo -= 1
            self.stamina_val -= 1
            if self.hit == True:
                self.health_val -= 1
        if self.stamina == 0 or self.ammo == 0:
            self.shoot = False
    
    def Recharge(self):
        self.recharge_cost = -2.5
        self.recharge_probability = 0.8
        if self.recharge == True:
            self.stamina_val+=1
            if self.stamina_val > 2: self.stamina_val=2

    def Dodge(self):
        self.dodge_cost = -2.5
        self.dodge_probability = 0.8 
        self.arrow_pick_probability = 0.8
        if self.dodge == True():
            self.stamina_val -= 1
            if self.ammo < 3:  self.ammo += 1


def main():
    ob = MD_saga_part_1()

if __name__ == '__main__':
    main()
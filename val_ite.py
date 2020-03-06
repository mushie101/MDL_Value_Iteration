import numpy as np

class MD_saga_part_1():
    def __init__(self):
        self.max_ammo = 3
        self.current_ammo = 3
        self.max_health = 100
        self.stamina = 100
        self.md_health = self.max_health
        self.final_reward = +10
        self.net_reward = 0
        self.actions = ['shoot', 'dodge', 'recharge']
        self.hit = True
        self.recharge = True
        self.dodge = True
        self.end_game = False
        # When MD health = 0, WIN_STATE
        # When Lero health = 0, LOSE_STATE

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


def main():
    ob = MD_saga_part_1()

if __name__ == '__main__':
    main()
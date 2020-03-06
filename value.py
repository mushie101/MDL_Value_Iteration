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



def value_iteration():
    V=np.zeroes()

def update_q(self, state, action, reward, new_state):
        self.Q_table[state][action] += self.lr * (reward + self.discount * np.max(self.Q_table[new_state]) - self.Q_table[state][action])




if __name__=='__main__':
    res=''
    main()

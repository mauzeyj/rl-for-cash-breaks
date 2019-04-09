import numpy as np
from gym import spaces
from gym.utils import seeding


class cash_breaks():
    def __init__(self):
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=-10000, high=10000, shape=(100,3), dtype=np.float32)
        self.state = None
        self.target_value = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self): # get dollar values
        start = np.zeros(100)
        values = cash_breaks.dollar_values()
        start[0:values.shape[0],] = values
        self.state = np.array(
            [twenty_one.card(self), twenty_one.card(self)])  # dealer player reward done info
        return self.state

    def dollar_values(self):
        return np.random.random_integers(low=-6000, high=6000, size=(cash_breaks.number_of_rows(), 1))

    def number_of_rows(self):
        return np.random.randint(10,80)

    def sum_value(self):

    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid" % (action, type(action))
        state = self.state
        dealer, player = state
        reward = 0
        done = False
        if action == 1:
            player = player + twenty_one.draw(self)
            if player > 21:
                reward = -1
                done = True
            if player < 1:
                reward = -1
                done = True
        if action == 0:
            while dealer < 17:
                dealer = dealer + twenty_one.draw(self)
            if dealer > 21:
                reward = 1
            elif dealer == player:
                reward = 0
            elif dealer > player:
                reward = -1
            elif player > dealer:
                reward = 1
            done = True
        self.state = np.array([dealer, player])
        return np.array(self.state), reward, done, {}

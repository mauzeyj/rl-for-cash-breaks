import numpy as np
from gym import spaces
from gym.utils import seeding


class cash_breaks():
    def __init__(self):
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=-10000, high=10000, shape=(100,3), dtype=np.float32)
        self.state = None
        self.target_value = None
        self.old_value = None
        self.new_value = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        """
        Creates matrix with 3 columns: dollar values, flag to clear, cursor location indicated by 1
        :return: matrix
        """
        start = np.zeros(100)
        values = cash_breaks.dollar_values(self)
        self.target_value = values.sum()
        values = np.concatenate([values, np.random.randint(low=-4000, high=6000, size=np.random.randint(3))])
        start[0:values.shape[0],] = values
        matrix = np.vstack([start, np.zeros(100), np.zeros(100)]).T
        matrix[-1,-1] = 1
        self.state = matrix
        return self.state

    def dollar_values(self):
        return np.random.random_integers(low=-4000, high=6000, size=(cash_breaks.number_of_rows(self)))

    def number_of_rows(self):
        return np.random.randint(10,80)

    def sum_value_for_reward(self):
        return 1

    # def step(self, action):
    #     assert self.action_space.contains(action), "%r (%s) invalid" % (action, type(action))
    #     state = self.state
    #     dealer, player = state
    #     reward = 0
    #     done = False
    #     if action == 1:
    #         player = player + twenty_one.draw(self)
    #         if player > 21:
    #             reward = -1
    #             done = True
    #         if player < 1:
    #             reward = -1
    #             done = True
    #     if action == 0:
    #         while dealer < 17:
    #             dealer = dealer + twenty_one.draw(self)
    #         if dealer > 21:
    #             reward = 1
    #         elif dealer == player:
    #             reward = 0
    #         elif dealer > player:
    #             reward = -1
    #         elif player > dealer:
    #             reward = 1
    #         done = True
    #     self.state = np.array([dealer, player])
    #     return np.array(self.state), reward, done, {}

env = cash_breaks()
env.reset()
import sys
import numpy as np


class QAgent(object):
    def __init__(self, server_config, train_config):
        self.cache_size = server_config['size']
        self.id = server_config['id']
        self.state_dim = server_config['state_dim']
        self.action_dim = server_config['action_dim']
        self.penalty = server_config['penalty']

        self.sigma2 = train_config['sigma2']
        self.isUpdateActor = True
        self.init_seqCnt = 0

        self.dataBuf = 0
        self.sinr = 0
        self.power = np.zeros(self.action_dim)
        self.reward = 0
        self.state = []

        # pre-defined param
        self.k = 1e-27
        self.t = 0.001
        self.L = 500




# #Abstract class
# class CacheAgent(object):
#     def __init__(self, n_actions): pass
#     def choose_action(self, observation): pass
#     def store_transition(self, s, a, r, s_): pass

# class ReflexAgent(CacheAgent):
#     def __init__(self, n_actions): pass
#
#     @staticmethod
#     def _choose_action(n_actions): pass
#
# class LearnerAgent(CacheAgent):
#     def __init__(self, n_actions): pass
#     def learn(self): pass


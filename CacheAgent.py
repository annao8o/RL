import sys
import numpy as np

'''
class MECTerm(object):
    def __init__(self, server_config, train_config, num_data):
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
        self.l_i = None
        self.reward = 0
        self.popularity = []
        self.state = []
        self.indicator = np.zeros(num_data)   #matrix로 초기화하기

        # pre-defined param
        self.k = 1e-27
        self.t = 0.001
        self.L = 500

    # def ca

    def setState(self, popularity, l_i):    #l_i: sub-region id
        self.popularity = popularity
        self.l_i = l_i
        self.state = np.array([self.popularity, self.l_i, self.indicator])


class MECTermRL(MECTerm):
    def __init__(self, sess, user_config, train_config):
        MECTerm.__init__(self, user_config, train_config)
        self.sess = sess
        self.agent =

# Simulation Environment
class CtrlSvrEnv(object):
    def __init__(self, svr_list, num_att, sigma2, max_len):
        self.svr_list = svr_list
        self.num_svr = len(svr_list)
        self.num_att = num_att
        self.sigma2 = sigma2
        self.count = 0
        self.seqCount = 0
        self.max_len = max_len

    def init_target_network(self):
        for svr in self.svr_list:
            svr.agent.init_target_network()

    def step_transmit(self, isRandom=True):
        rewards = np.zeros(self.num_svr)
        isOverflows = np.zeros(self.num_svr)

        self.count += 1

        # feedback the


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
'''

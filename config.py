import random
import numpy as np

svr_num = 4
file_num = 50
file_size = np.array([random.randint(10, 200) for _ in range(file_num)])
cache_size = 5
popularity = []#random으로 발생시키기

num_episodes = 2000
NO_REWARD = 0




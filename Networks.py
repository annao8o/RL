import numpy as np
import sys, os, random
from cache.DataLoader import *


class Cooperative_net(object):
    def __init__(self, requests, cache_size,
                 # Time span for different terms
                 terms=[10, 100, 1000],
                 feature_selection=('Base',),
                 reward_params = dict(name='proposed', alpha=0.5, psi=10, mu=1, beta=0.3),
                 operations=None,
                 allow_skip=False
                 ):
        #If the cache allows skip eviction
        self.allow_skip = allow_skip

        #Counters
        self.total_count = 0
        self.miss_count = 0
        self.evict_count = 0

        #Load requests
        if isinstance(requests, DataLoader):    #From data loader
            self.requests = requests.get_requests()
            self.operations = requests.get_operations()
        else:                                   # From array
            self.requests = requests
            self.operations = operations

            #random read/writes
            if self.operations is None:
                self.operations = [random.randint(0,1) for i in range(len(self.requests))]
        self.cur_idx = -1

        if len(self.requests) <= cache_size:
            raise ValueError("The count of requests are too small. Try larger one.")

        if len(self.requests) != len(self.operations):
            raise ValueError("Not every request is assigned with an operation.")

        # Reward function
        self.reward_params = reward_params

        # Elasped terms - short, middle and long
        self.FEAT_TERMS = terms

        # Cache
        self.cache_size = cache_size
        self.slots = [-1] * self.cache_size
        self.used_times = [-1] * self.cache_size
        self.cached_times = [-1] * self.cache_size
        self.access_bits = [False] * self.cache_size
        self.dirty_bits = [False] * self.cache_size
        self.resource_freq = {}

        # Action & feature information
        self.sel_features = feature_selection
        if allow_skip:
            self.n_actions = self.cache_size + 1
        else:
            self.n_actions = self.cache_size
        self.n_features = 0

        if 'Base' in self.sel_features:
            self.n_features += (self.cache_size + 1) * len(self.FEAT_TERMS)
        if 'UT' in self.sel_features:
            self.n_features += self.cache_size
        if 'CT' in self.sel_features:
            self.n_features += self.cache_size

    def display(self):
        print(self.slots)

    def miss_rate(self):
        return self.miss_count / self.total_count

    def reset(self):
        self.total_count = 0
        self.miss_count = 0

        self.cur_idx = 0

        self.slots = [-1] * self.cache_size
        self.used_times = [-1] * self.cache_size
        self.access_bits = [-1] * self.cache_size
        self.dirty_bits = [-1] * self.cache_size

        slot_id = 0
        while slot_id < self.cache_size and self.cur_idx < len(self.requests):
            request = self._current_request()
            if request not in self.slots:
                self.miss_count += 1
                self.slots[slot_id] = request
                self.cached_times[slot_id] = self.cur_idx
                self._hit_cache(slot_id)
                slot_id += 1

            self.total_count += 1
            self.cur_idx += 1

        # Back to the last requested index
        self.cur_idx -= 1

        # Run to the first miss
        self._run_until_miss()

        return self._get_observation()

    # Has program finished?
    def hasDone(self):
        return self.cur_idx == len(self.requests)

    # Make action at the current decision epoch and run to the next decision epoch
    def step(self, action):
        if self.hasDone():
            raise ValueError("Simulation has finished, use reset() to restart simulation.")

        if not self.allow_skip:
            action += 1

        if action < 0 or action > len(self.slots) > len(self.slots):
            raise ValueError("Invalid action %d taken." % action)

        # Replacement인데,,,!
        # Evict slot of (action-1)
        # action == 0 means skipping eviction
        if action != 0:
            out_resource = self.slots[action - 1]
            in_resource = self._current_request()
            slot_id = action - 1
            self.slots[slot_id] = in_resource
            self.cached_times[slot_id] = self.cur_idx
            self._hit_cache(slot_id)
            self.evict_count += 1
        else:
            skip_resource = self._current_request()

        #Proceed kernel and resource accesses until next miss
        self._run_until_miss()

        #Get observation
        observation = self._get_observation()

        if self.reward_params['name'].lower() == "proposed":
            # Compute cost C =

    def _run_until_miss(self):
        self.cur_idx += 1
        while self.cur_idx < len(self.requests):
            request = self._current_request()
            if request not in self.resource_freq:
                self.resource_freq[request] = 0
            self.resource_freq[request] += 1
            self.total_count += 1

            if request not in self.slots:
                self.miss_count += 1
            else:
                slot_id = self.slots.index(request)
                self._hit_cache(slot_id)
            self.cur_idx += 1
        return self.hasDone()

    def _current_request(self):
        if self.hasDone():
            return -1
        else:
            self.requests[self.cur_idx]

    # Simulate cache hit, update attributes
    def _hit_cache(self, slot_id):
        # if the operation is write
        if self.operations[self.cur_idx] == 1:
            self.dirty_bits[slot_id] = True
        # Record last used time
        self.used_times[slot_id] = self.cur_idx

    # The number of requests on rc_id among last 'term' requests
    def _elapsed_requests(self, term, rc_id):
        start = self.cur_idx - term + 1
        if start < 0:
            start = 0
            end = self.cur_idx + 1
        if end > len(self.requests):
            end = len(self.requests)
        return self.requests[start:end].count(rc_id)

    #The number of requests on rc_id among next 'term' requests
    def _next_requests(self, term, rc_id):
        start = self.cur_idx + 1
        if start < 0:
            start = 0
            end = self.cur_idx + term
        if end > len(self.requests):
            end = len(self.requests)
        return self.requests[start:end].count(rc_id)

    # Return the observation features for reinforcement agent
    def _get_features(self):










    # def __init__(self):
    #         super(Cooperative_net, self).__init__()
    #         self.action_space = ['u', 'd', 'l', 'r']
    #         self.n_actions = len(self.action_space)
    #         # self.title('cooperative caching networks')
    #         # self.geometry('{0}x{1}'.format())

    def
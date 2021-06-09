from Networks import *

class mecAgent(object):
    def __init__(self, mec_id):
        self.mec_id = mec_id
        self.region_id = None

    def set_region(self, region_id):
        self.region_id = region_id

    def act(self, state, ava_actions):  # avaliable actions: caching or not
        for action in ava_actions:
            pass


from Networks import *
from config import *

class mecAgent(object):
    def __init__(self, mark):
        self.mark = mark
    #     self.region_id = None
    #
    # def set_region(self, region_id):
    #     self.region_id = region_id

    def act(self, state, ava_actions):  # avaliable actions: caching or not
        for action in ava_actions:
            nstate = after_action_state(state, action)
            gstatus = check_network_status(nstate[0])
            if gstatus > 0:
                return


def run():
    start_mark = 0
    env = cachingEnv()
    agents = [mecAgent(i) for i in range(svr_num)]

    for _ in range(num_episodes):
        env.set_start_mark(start_mark)
        state = env.reset()
        while not env.done:
            _, mark = state

            agent = agent_by_mark(agents, mark)
            ava_actions = env.available_actions()
            action = agent.act(state, ava_actions)
            state, reward, done, info = env.step(action)
            env.render()

        env.show_result(True, mark, reward)

        start_mark = next_mark(start_mark)



if __name__ == '__main__':
    run()


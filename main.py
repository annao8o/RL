from RL_agent import QLearningTable
from Networks import Cooperative_net

def update():
    for episode in range(100):
        observation = env.reset()

        while True:
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            observation_, reward, done = env.step(action)

            RL.learn(str(observation), action, reward, str(observation_))

            observation = observation_

            if done:
                break


if __name__ == "__main__":
    env = Cooperative_net()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()
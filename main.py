import os
import time
import click
from manager import ConfigManager


@click.command()
@click.argument('config_name')
@click.option('-m', '--model-name', default=None)
def run(config_name, model_name=None):
    cfg = ConfigManager.load(config_name)

    if model_name is None:
        model_name = '-'.join([
            cfg.env_name.lower(),
            cfg.policy_name.replace('_', '-'),
            os.path.splitext(os.path.basename(config_name))[0] if config_name else 'default',
            str(int(time.time()))
        ])

    model_name = model_name.lower()
    cfg.start_training(model_name)


if __name__ == '__main__':
    run()


'''
from Networks import cachingEnv
from _collections import defaultdict

def update_Q(s, r, a, s_next, done):
    max_q_next = max([Q[s_next, a] for a in actions])

    # Do not include the next state's value if currently at the terminal state.
    Q[s, a] += alpha * (r + gamma * max_q_next * (1.0 - done) - Q[s, a])


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
    env = cachingEnv()
    actions = range(env.action_space)


    # RL = QLearningTable(actions=list(range(env.n_actions)))
    #
    # env.after(100, update)
    # env.mainloop()
'''
#coding: utf-8
import random
from environment import Environment

class Agent():
    def __init__(self, env):
        self.actions = env.actions

    def policy(self, state):
        return random.choice(self.actions)

def main():
    grid = [
    [0, 0, 0, 1],
    [0, 9, 0, -1],
    [0, 0, 0, 0]
    ]
    env = Environment(grid)
    agent = Agent(env)

    lastRewards = []
    for i in range(10):
        state = env.reset()
        total_reward = 0
        done = False

        lastReward = 0
        while not done:
            action = agent.policy(state)
            #print(action)
            next_state, reward, done = env.step(action)
            total_reward += reward
            state = next_state
            lastReward = reward
        lastRewards.append(lastReward)

    #for x in lastRewards:
        #print(x)
    print("episode {}: Agent gets {:.2g} reward.".format(i, total_reward))

if __name__ == "__main__":
    main()

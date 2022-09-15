import numpy as np

from CONFIG import *


def find_max_reward(env):
    
    episode_rewards = []
    for e in range(1000):
        rewards = []
        state = env.reset()
        while True:
            next_state, reward, done, _ = env.step(BEST_POLICY[state])
            rewards.append(reward)
            if done:
                break
            state = next_state
            
        episode_rewards.append(sum(rewards))
        
    return np.mean(episode_rewards)
    
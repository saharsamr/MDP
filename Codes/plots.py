import matplotlib.pyplot as plt
import numpy as np


def get_average(repeats_rewards, window_size):

    repeats_rewards = np.array(repeats_rewards)
    episodes = repeats_rewards.shape[1]
    averaged_rewards = [np.mean(repeats_rewards[:,episode]) for episode in range(episodes)]
    averaged_rewards = [np.mean(averaged_rewards[start:start+window_size]) for start in range(episodes-window_size+1)]
    
    return averaged_rewards
    
    
def get_cumulative_regret(averaged_rewards, max_expected_reward):
    
    regret = [max_expected_reward - reward for reward in averaged_rewards]
    cumulative_regret = [regret[0]]
    for i in range(1, len(regret)):
        cumulative_regret.append(cumulative_regret[i-1]+regret[i])
        
    return cumulative_regret


def plot_total_episode_rewards(repeats_rewards1, repeats_rewards2, max_expected_reward, label1, label2, window_size=1):
        
    averaged_rewards1 = get_average(repeats_rewards1, window_size)
    averaged_rewards2 = get_average(repeats_rewards2, window_size)
    
    plt.plot(averaged_rewards1, label=label1)
    plt.plot(averaged_rewards2, label=label2)
    plt.plot([max_expected_reward for _ in averaged_rewards1], label='expected maximum reward')
    plt.xlabel('episodes')
    plt.ylabel('rewards')
    plt.legend()
    plt.show()
    
    
def plot_regret(repeats_rewards1, repeats_rewards2, max_expected_reward, label1, label2, window_size=1):
    
    averaged_rewards1 = get_average(repeats_rewards1, 1)
    averaged_rewards2 = get_average(repeats_rewards2, 1)
    
    cumulative_regret1 = get_cumulative_regret(averaged_rewards1, max_expected_reward)
    cumulative_regret2 = get_cumulative_regret(averaged_rewards2, max_expected_reward)
        
    plt.plot(cumulative_regret1, label=label1)
    plt.plot(cumulative_regret2, label=label2)
    plt.xlabel('episodes')
    plt.ylabel('regret')
    plt.legend()
    plt.show()
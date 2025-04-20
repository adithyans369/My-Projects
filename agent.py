import numpy as np
import os
import random

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_state_key(self, state):
        return tuple(state)

    def ensure_state(self, key, actions):
        if key not in self.q_table:
            self.q_table[key] = {a: 0.0 for a in actions}

    def choose_action(self, state, available_actions):
        key = self.get_state_key(state)
        self.ensure_state(key, available_actions)

        if random.random() < self.epsilon:
            return random.choice(available_actions)
        return max(self.q_table[key], key=self.q_table[key].get)

    def update(self, state, action, reward, next_state, done, next_available_actions):
        key = self.get_state_key(state)
        next_key = self.get_state_key(next_state)

        self.ensure_state(key, [action] + next_available_actions)
        self.ensure_state(next_key, next_available_actions)

        current_q = self.q_table[key][action]
        future_q = 0 if done else max(self.q_table[next_key].values())

        self.q_table[key][action] = current_q + self.alpha * (reward + self.gamma * future_q - current_q)

    def save(self, filename='q_table.npy'):
        np.save(filename, self.q_table)

    def load(self, filename='q_table.npy'):
        if os.path.exists(filename):
            self.q_table = np.load(filename, allow_pickle=True).item()
            print(f"[INFO] Loaded Q-table from {filename}")
        else:
            print(f"[WARNING] {filename} not found. Starting with an empty Q-table.")

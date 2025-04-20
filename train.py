'''def train(episodes=10000):
    agent = QLearningAgent()
    try:
        agent.load()
    except:
        pass

    for episode in range(episodes):
        env = TicTacToe()
        state = env.get_state()
        done = False

        while not done:
            available = env.available_actions()
            action = agent.choose_action(state, available)
            env.make_move(action, player=1)
            reward = 0

            if env.done:
                reward = 1 if env.winner == 1 else 0
            else:
                opponent_action = agent.choose_action(env.get_state(), env.available_actions())
                env.make_move(opponent_action, player=-1)
                if env.done:
                    reward = -1 if env.winner == -1 else 0

            next_state = env.get_state()
            next_available = env.available_actions()

            agent.update(state, action, reward, next_state, env.done, next_available)
            state = next_state

        if episode % 500 == 0:
            print(f"[INFO] Episode {episode}/{episodes} completed")

    agent.save()
    print("[✅] Training complete. Q-table saved.")'''

import numpy as np
from agent import QLearningAgent
from tictactoe_env import TicTacToe

EPISODES = 100_000
SAVE_FILE = "q_table.npy"
epsilon = 1.0
min_epsilon = 0.01
decay_rate = 0.9995
learning_rate = 0.1
discount_factor = 0.9

env = TicTacToe()
agent = QLearningAgent(learning_rate, discount_factor)

# Load Q-table if exists
try:
    agent.q_table = np.load(SAVE_FILE, allow_pickle=True).item()
    print("[INFO] Loaded existing Q-table.")
except FileNotFoundError:
    print("[WARNING] Q-table not found. Starting with an empty Q-table.")

for episode in range(EPISODES):
    state = env.reset()
    done = False

    while not done:
        available_actions = env.available_actions()
        action = agent.select_action(state, available_actions, epsilon)

        next_state, reward, done = env.step(action)
        next_available_actions = env.available_actions()

        agent.update(state, action, reward, next_state, next_available_actions)

        state = next_state

    epsilon = max(min_epsilon, epsilon * decay_rate)

    if episode % 10000 == 0:
        print(f"[TRAINING] Episode {episode}, Epsilon: {epsilon:.4f}")

# Save trained Q-table
np.save(SAVE_FILE, agent.q_table)
print("[INFO] Training completed and Q-table saved.")

cd your_project_folder

git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/tic-tac-toe-rl.git
git branch -M main
git push -u origin main

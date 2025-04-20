import streamlit as st
from agent import QLearningAgent
from tictactoe_env import TicTacToe

st.title("Tic Tac Toe with Q-Learning Agent")

if "env" not in st.session_state:
    st.session_state.env = TicTacToe()
    st.session_state.agent = QLearningAgent()
    try:
        st.session_state.agent.load()
    except:
        pass

env = st.session_state.env
agent = st.session_state.agent

st.write("You play as: ❌ (1)")

cols = st.columns(3)
for idx in range(9):
    i, j = divmod(idx, 3)
    cell_val = env.get_state()[idx]
    label = "⭕" if cell_val == 1 else "❌" if cell_val == -1 else " "
    if cols[j].button(label, key=f"cell_{idx}"):
        if env.done:
            st.warning("Game over! Click 'Restart' to play again.")
        elif env.board[idx] == 0:
            env.make_move(idx, player=-1)
            if not env.done:
                action = agent.choose_action(env.get_state(), env.available_actions())
                env.make_move(action, player=1)

if env.done:
    if env.winner == -1:
        st.success("You win! 🎉")
    elif env.winner == 1:
        st.error("Agent wins! 🤖")
    else:
        st.info("It's a draw! 🤝")

if st.button("Restart"):
    st.session_state.env = TicTacToe()

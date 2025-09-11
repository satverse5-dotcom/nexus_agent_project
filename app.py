import streamlit as st
from agent import create_agent

st.set_page_config(page_title="NexusAgent Showcase", layout="wide")

st.title("🧠 NexusAgent: Autonomous AI Assistant")

# Initialize the agent and store it in session state
if 'agent_executor' not in st.session_state:
    st.session_state.agent_executor = create_agent()

user_goal = st.text_input("Enter your high-level goal:", placeholder="e.g., Research the top 3 electric cars in India and compare their range and price.")

if st.button("Run Agent"):
    if user_goal:
        with st.spinner("NexusAgent is thinking..."):
            try:
                # Use a container for the verbose output
                with st.chat_message("assistant", avatar="🧠"):
                    st.write(f"Executing goal: *{user_goal}*")
                    # To capture verbose output in Streamlit, we need a custom handler.
                    # For this guide, we will just show the final answer, which is cleaner.
                    result = st.session_state.agent_executor.invoke({"input": user_goal})
                    st.success("Goal achieved! Here is the final answer:")
                    st.markdown(result['output'])
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a goal.")
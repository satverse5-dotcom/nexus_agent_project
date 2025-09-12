import streamlit as st

st.set_page_config(page_title="🧠 NexusAgent", layout="wide")

st.title("🧠 NexusAgent: Autonomous AI Assistant")
st.write("Welcome! This is the starting point for your autonomous AI project.")

# Input from user
user_goal = st.text_area("Enter your research goal:")

if st.button("Run Agent"):
    st.info("🚀 Agent would start running here...")
    # Placeholder for actual agent logic
    st.success("✅ Demo complete! Integrate your agent code here.")

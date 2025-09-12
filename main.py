# main.py

# --- 1. Imports ---
# Used to load the .env file and get the API key
import os
from dotenv import load_dotenv

# The main LangChain components
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain import hub

# --- 2. Setup ---
# Load the environment variables from the .env file
load_dotenv()

# Check if the OpenAI API key is available.
if os.getenv("OPENAI_API_KEY") is None:
    print("Error: OPENAI_API_KEY is not set in the .env file.")
    exit()

# --- 3. Initialize the LLM (The "Brain") ---
# We use ChatOpenAI, which is the standard for interacting with OpenAI models.
# 'temperature=0' makes the model's responses more deterministic and less random.
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# --- 4. Define the Tools (The "Toolbox") ---
# These are the actions the agent can take.
# DuckDuckGoSearchRun is a free search tool that doesn't need an API key.
search = DuckDuckGoSearchRun()

# The tools are provided to the agent as a list.
tools = [search]

# --- 5. Create the Agent (The "Worker") ---
# We pull a pre-built ReAct prompt template from the LangChain hub.
# This prompt is the core instruction set that tells the LLM how to behave as an agent.
prompt = hub.pull("hwchase17/react")

# We create the agent by combining the LLM, the tools, and the prompt.
agent = create_react_agent(llm, tools, prompt)

# The AgentExecutor is what actually runs the agent's reasoning loop.
# 'verbose=True' is CRITICAL for debugging. It prints the agent's thoughts to the console.
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- 6. Run the Agent ---
# Define the high-level goal you want the agent to achieve.
goal = "Find top 5G smartphones in India launched in the last 6 months and compare them."

# 'invoke' starts the agent's reasoning loop.
# The input is passed as a dictionary.
result = agent_executor.invoke({"input": goal})

# --- 7. Print the Final Answer ---
# The agent's final, summarized answer is stored in the 'output' key of the result.
print("\n--- FINAL ANSWER ---")
print(result['output'])
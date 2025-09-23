from typing import TypedDict, Annotated, Sequence
import operator
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

if not gemini_key:
    raise RuntimeError("❌ GEMINI_API_KEY not found in .env file")

# --- Agent State ---
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

class LangGraphAgent:
    """
    NexusAgent powered by LangGraph + LangChain ChatGoogleGenerativeAI.
    """

    def __init__(self, llm: ChatGoogleGenerativeAI = None):
        # If no LLM is passed, use default Gemini model
        self.llm = llm or ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.7,
            google_api_key=gemini_key   # ✅ Explicit key usage
        )
        self.graph = self._build_graph()

    def _build_graph(self):
        graph = StateGraph(AgentState)
        graph.add_node("agent", self.call_model)
        graph.set_entry_point("agent")
        graph.add_edge("agent", END)
        return graph.compile()

    def call_model(self, state: AgentState):
        last_message = state["messages"][-1].content
        response = self.llm.invoke(last_message)
        return {"messages": [HumanMessage(content=response.content)]}

    def run(self, query: str):
        initial_input = [HumanMessage(content=query)]
        return self.graph.stream({"messages": initial_input})

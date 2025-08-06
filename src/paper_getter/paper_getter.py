from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, create_react_agent
from langchain_core.messages import SystemMessage
from langchain.chat_models.base import init_chat_model

from pydantic import BaseModel, Field

from typing import List, Optional

from src.utils.util import create_model
from src.utils.state import InputState, SystemState
from src.utils.prompts import agent_prompt
from src.utils.tools_all import search


model = init_chat_model(
    model="gemini-2.0-flash", model_provider="google_genai", temperature=0.0
)
tools = [search]

model = model.bind_tools(tools)


def get_paper(state: SystemState) -> SystemState:
    """Function to get a paper based on the subtopics."""
    # system_prompt = SystemMessage(
    #     "You are a helpful AI assistant, please respond to the users query to the best of your ability!"
    # )

    # response = model.invoke([system_prompt] + state["subtopics"])
    # state["subtopics"] = response
    # TODO: Implement the logic to get papers based on subtopics. USING for loops and arxiv tools
    agent_executor = create_react_agent(model, tools)
    print("agent created!!!")
    state["topic"] = agent_executor.invoke({"messages": state["topic"]})["messages"][
        -1
    ].content
    print(state)
    return state


def should_continue(state: SystemState) -> str:
    """Decide whether to continue or not based on the last response."""
    print(state["subtopics"].tool_calls)
    if not state["subtopics"].tool_calls:
        return "end"
    # Otherwise if there is, we continue
    else:
        return "continue"


graph = StateGraph(SystemState, input_schema=SystemState)
graph.add_node("get_paper", get_paper)
# graph.add_node("tools", ToolNode(tools, messages_key="subtopics"))
graph.set_entry_point("get_paper")
graph.set_finish_point("get_paper")
# graph.add_conditional_edges(
#     "get_paper",
#     should_continue,
#     {
#         "continue": "tools",
#         "end": END,
#     },
# )
# graph.add_edge("tools", "get_paper")
graph = graph.compile()

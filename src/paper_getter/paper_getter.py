from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, create_react_agent
from langchain_core.messages import SystemMessage
from langchain.chat_models.base import init_chat_model

from pydantic import BaseModel, Field

from typing import List, Optional

from src.paper_getter.tools import get_papers
from src.paper_getter.prompt import getting_papers_prompt, enough_data_prompt
from src.paper_getter.output_schemas import EnoughDataCheck

from src.utils.util import create_model
from src.utils.state import InputState, SystemState
from src.utils.prompts import agent_prompt


model = init_chat_model(
    model="gemini-2.0-flash", model_provider="google_genai", temperature=0.0
)
tools = [get_papers]

model = model.bind_tools(tools)


def get_paper(state: SystemState) -> SystemState:
    """Function to get a paper based on the subtopics."""
    agent_executor = create_react_agent(model, tools, prompt=getting_papers_prompt)
    print("agent created!!!")
    papers = {}
    subtopics = state.get("subtopics", [])
    if not subtopics:
        state["papers"] = {
            state["topic"]: agent_executor.invoke({"messages": state["topic"]})[
                "messages"
            ][-1].content
        }
    else:
        for subtopic in subtopics:
            paper_for_subtopic = agent_executor.invoke({"messages": subtopic})[
                "messages"
            ][-1].content
            papers[subtopic] = paper_for_subtopic
        state["papers"] = papers
    print(state)
    return state


def check_enough_data(state: SystemState) -> bool:
    """Check if there is enough data to proceed with the next step."""
    model = create_model(prompt=enough_data_prompt)
    model_chain = enough_data_prompt | model.with_structured_output(EnoughDataCheck)
    result = model_chain.invoke(
        {
            "topic": state["topic"],
            "subtopics": state.get("subtopics", []),
            "papers": state.get("papers", {}).values(),
        }
    )
    print("Enough data check result:", result)
    return result.enough_data and result.does_overlap


graph = StateGraph(SystemState, input_schema=SystemState)
graph.add_node("get_paper", get_paper)
# graph.add_node("tools", ToolNode(tools, messages_key="subtopics"))
graph.set_entry_point("get_paper")
graph.add_conditional_edges(
    "get_paper",
    check_enough_data,
    {
        False: "get_paper",
        True: END,
    },
)
graph.set_finish_point("get_paper")

paper_getter = graph.compile()

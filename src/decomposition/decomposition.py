from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field
from typing import List, Optional
from src.utils.util import create_model
from src.utils.state import InputState, SystemState
from src.decomposition.state import DecompositionState
from src.decomposition.output_schemas import SubtopicOutput, IsRelevantOutput
from src.decomposition.prompts import create_subtopic_prompt, check_relevance_prompt


def create_subtopics(state: InputState) -> SystemState:
    """Create subtopics from the main topic."""
    topic = state["topic"]
    subtopics = state.get("subtopics", [])
    llm = create_model(prompt=create_subtopic_prompt)
    llm = create_subtopic_prompt | llm.with_structured_output(SubtopicOutput)
    response = llm.invoke(
        {"topic": topic, "subtopics": subtopics},
    )
    print(response)
    subtopics.extend(response.subtopics)
    return {
        "topic": topic,
        "subtopics": subtopics,
    }


def check_relevance(state: DecompositionState) -> str:
    """Check if the subtopic is relevant to the main topic."""
    subtopics = state["subtopics"]
    topic = state["topic"]
    llm = create_model(prompt=check_relevance_prompt)
    llm = check_relevance_prompt | llm.with_structured_output(IsRelevantOutput)

    response = llm.invoke(
        {"topic": topic, "subtopics": subtopics},
    )
    print(response)
    for subtopic, is_relevant in zip(state["subtopics"], response.is_relevant):
        print(f"Subtopic: {subtopic}, Relevant: {is_relevant}")
        if not response.is_relevant:
            return "create_subtopics"
    return END


graph = StateGraph(SystemState, input_schema=InputState)

graph.add_node("create_subtopics", create_subtopics)
graph.add_edge(START, "create_subtopics")
graph.add_conditional_edges(
    "create_subtopics",
    check_relevance,
    {"create_subtopics": "create_subtopics", END: END},
)
graph = graph.compile()

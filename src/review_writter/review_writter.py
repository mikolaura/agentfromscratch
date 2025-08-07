from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field

from src.review_writter.prompts import prompt
from src.review_writter.output_schemas import Review


from src.utils.state import SystemState
from src.utils.util import create_model


def review_writter(state: SystemState) -> SystemState:
    """Function to write a review based on the papers collected."""
    structured_papers = ""
    papers = state.get("papers", {})
    for subtopic, paper_list in papers.items():
        structured_papers += f"Subtopic: {subtopic}\n"
        for paper in paper_list:
            structured_papers += f"- {paper}\n"

    model = create_model(prompt)
    model = prompt | model.with_structured_output(Review)
    response = model.invoke(
        {
            "papers": structured_papers,
            "topic": state["topic"],
            "subtopics": state["subtopics"],
        }
    )
    print(response)
    state["review"] = response.review
    return state


review = StateGraph(SystemState)
review.add_node("review_writter", review_writter)
review.set_entry_point("review_writter")
review.set_finish_point("review_writter")

review = review.compile()

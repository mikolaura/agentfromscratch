from typing import TypedDict, Optional, Any, Dict
from langchain_core.messages import BaseMessage


class InputState(TypedDict):
    """Input state for the decomposition graph."""

    topic: str


class SystemState(TypedDict):
    """System state for the decomposition graph."""

    topic: str
    """List of subtopics derived from the main topic."""
    subtopics: Optional[list[str]] = []
    # EXAMPLE: {"subtopic_name": ["paper1", "paper2", ...]}
    papers: Optional[Dict[str, list[str]]] = []

    review: Optional[str] = None

from typing import TypedDict, Optional, Any
from langchain_core.messages import BaseMessage


class InputState(TypedDict):
    """Input state for the decomposition graph."""

    topic: str


class SystemState(TypedDict):
    """System state for the decomposition graph."""

    topic: str
    """List of subtopics derived from the main topic."""
    subtopics: Optional[list[str]] = []

    papers: Optional[list[str]] = []

    # messages: Optional[list[BaseMessage]] = None

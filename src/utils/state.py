from typing import TypedDict


class InputState(TypedDict):
    """Input state for the decomposition graph."""

    topic: str


class SystemState(TypedDict):
    """System state for the decomposition graph."""

    topic: str
    """List of subtopics derived from the main topic."""
    subtopics: list[str] = []

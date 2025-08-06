from typing import TypedDict, Sequence, List, Union


class DecompositionState(TypedDict):
    """State for the decomposition graph.

    This state holds the topic and a list of subtopics.
    """

    topic: str
    subtopics: List[str]

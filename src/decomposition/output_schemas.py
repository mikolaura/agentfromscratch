from pydantic import BaseModel, Field
from typing import List, Optional


class SubtopicOutput(BaseModel):
    """Output model for subtopics."""

    subtopics: List[str] = Field(
        ...,
        description="List of subtopics derived from the main topic.",
    )


class IsRelevantOutput(BaseModel):
    """Output model for relevance check."""

    is_relevant: List[bool] = Field(
        ...,
        description="Indicates whether the subtopics is relevant to the main topic.",
    )

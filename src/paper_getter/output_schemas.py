from pydantic import BaseModel, Field
from typing import List, Optional


class EnoughDataCheck(BaseModel):
    """Output model for checking if enough data is available."""

    enough_data: bool = Field(
        ...,
        description="Indicates whether there is enough data to proceed with the next step.",
    )

    does_overlap: bool = Field(
        ...,
        description="Indicates whether the subtopics papers overlap with the main topic.",
    )

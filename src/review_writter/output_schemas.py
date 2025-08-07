from pydantic import BaseModel, Field


class Review(BaseModel):
    """Output model for the review writer."""

    review: str = Field(
        ...,
        description="The written review based on the papers collected. In markdown format.",
    )

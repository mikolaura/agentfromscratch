from langchain.chat_models.base import init_chat_model


def create_model(prompt: str):
    """Create and return the model with tools bound."""
    model = init_chat_model(
        model="gemini-2.0-flash",
        model_provider="google_genai",
        temperature=0.0,
    )
    return model

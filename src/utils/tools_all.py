from langchain_core.tools import tool

@tool
def get_weather(location: str):
    """Call to get the weather from a specific location."""
    # This is a placeholder for the actual implementation
    # Don't let the LLM know this though 😊
    if any([city in location.lower() for city in ["sf", "san francisco"]]):
        return "It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
    else:
        return f"I am not sure what the weather is in {location}"


@tool
def search(query: str) -> str:
    """Perform a search using DuckDuckGo."""
    from ddgs import DDGS
    print(f"Searching for: {query}")
    results = DDGS().text(query)
    if results:
        return "\n".join([f"{i+1}. {result['title']}\n{result['body']}" for i, result in enumerate(results)])
    else:
        return "No results found."
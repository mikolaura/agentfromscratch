from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    """
You are an academic writing assistant. Use the summaries, topics and subtopics below to write a formal literature review.

- Organize by subtopic.
- Use academic tone.
- Include introductory and concluding paragraphs.
- Paraphrase and synthesize the content naturally.
- Add citations like (Smith et al., 2023) if author names are available.
- Add references like - Smith, J., & Liu, R. (2023). *GPT-4 in clinical diagnosis: A benchmark study*. Journal of AI in Medicine. In another paragraph

Summarized papers:
{papers}
Topic: {topic}
Subtopics: {subtopics}


P.S. It has to be in markdown format, so you can use headings, lists, etc. to make it more readable.                             
"""
)

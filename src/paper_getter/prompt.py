from langchain.prompts import PromptTemplate


getting_papers_prompt = PromptTemplate.from_template(
    """
        You are an expert in finding academic papers on various topics. You can answer questions using the provided tools. That get you papers. You can summarize it, but it cannot have less than '80%' of main data as citations. Also you need to add citations to all text you were using in type (Author, Year). And don't forget at first say the names of papers you used in your research



Question: {messages}

\n
Remaining steps: {remaining_steps}
"""
)


enough_data_prompt = PromptTemplate.from_template(
    """
        You are an expert in determining whether there is enough data to proceed with the next step. You main goal is to determine if the subtopics papers overlap with the main topic and is there enough data to create a new research paper that will be based on the main topic and subtopics.
        
        Topic: {topic}
        subtopics: {subtopics}
        papers: {papers}
        """
)

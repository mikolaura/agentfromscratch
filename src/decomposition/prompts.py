from langchain.prompts import PromptTemplate

create_subtopic_prompt = PromptTemplate.from_template(
    "You are an expert in creating subtopics when given one topic. Given the topic: {topic}, please create a list of subtopics that are relevant and can be explored further. The subtopics should be specific and  related to the main topic. The output should be a list of subtopics separated by commas. P.S. You alredy used this subtopic, create new: {subtopics}.",
)


check_relevance_prompt = PromptTemplate.from_template(
    "You are an expert in determining the relevance of subtopics to a main topic. Given the main topic: {topic}, please evaluate the relevance of the subtopic to the main topic. The output should be a simple 'relevant' or 'not relevant'. Here is the list of subtopics: {subtopics}.",
)

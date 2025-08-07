from langchain.tools import tool
import arxiv
from pypdf import PdfReader
import os


@tool
def get_papers(topic: str) -> list:
    """Search for papers related to a given topic using an arxiv database.
    Args:
        topic (str): The topic to search for papers.
    Returns:
        papers(list): A list of papers related to the topic.

    """

    def extract_text_from_pdf(pdf_path):
        reader = PdfReader(pdf_path)
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text()
        return full_text

    client = arxiv.Client()

    search = arxiv.Search(
        query=topic,
        max_results=3,
    )
    papers = []
    results = client.results(search)
    for result in results:
        pdf_file = result.download_pdf()
        extracted_text = extract_text_from_pdf(pdf_file)
        papers.append(extracted_text)
        os.remove(pdf_file)
    return papers

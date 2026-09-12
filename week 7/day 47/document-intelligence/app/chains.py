from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0,
)

parser = StrOutputParser()


# 1. Information extraction
extraction_prompt = ChatPromptTemplate.from_template(
    """
    Analyze this document and extract the most important information.

    Include:
    - Document purpose
    - Main subject
    - Important facts
    - Important people, organizations, or entities
    - Important dates or numbers

    Document:
    {document}
    """
)

extraction_chain = extraction_prompt | model | parser


# 2. Summary
summary_prompt = ChatPromptTemplate.from_template(
    """
    Create a concise but informative summary of this document.

    Document:
    {document}
    """
)

summary_chain = summary_prompt | model | parser


# 3. Key topics
topics_prompt = ChatPromptTemplate.from_template(
    """
    Identify the most important topics discussed in this document.

    Return them as a numbered list.

    Document:
    {document}
    """
)

topics_chain = topics_prompt | model | parser


# 4. Action items
actions_prompt = ChatPromptTemplate.from_template(
    """
    Identify all actionable tasks, requirements, deadlines,
    recommendations, or next steps mentioned in this document.

    If there are no clear action items, say:
    "No clear action items found."

    Document:
    {document}
    """
)

def analyze_document(text: str) -> dict:
    extraction = extraction_chain.invoke({"document": text})

    summary = summary_chain.invoke({"document": text})

    topics = topics_chain.invoke({"document": text})

    actions = actions_chain.invoke({"document": text})

    return {
        "extraction": extraction,
        "summary": summary,
        "topics": topics,
        "actions": actions,
    }

actions_chain = actions_prompt | model | parser
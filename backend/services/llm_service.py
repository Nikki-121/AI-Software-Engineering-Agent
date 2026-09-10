import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def get_llm():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not configured. "
            "Add it to the backend .env file."
        )

    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

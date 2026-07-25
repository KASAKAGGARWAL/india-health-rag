import os

from dotenv import load_dotenv
from groq import Groq

from config import LLM_MODEL
from prompts import SYSTEM_PROMPT, USER_PROMPT

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(question: str, context: str) -> str:
    """
    Generates an answer using the retrieved context.
    """

    system_prompt = SYSTEM_PROMPT.format(
        context=context
    )

    user_prompt = USER_PROMPT.format(
        question=question
    )

    response = client.chat.completions.create(
        model=LLM_MODEL,
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response.choices[0].message.content
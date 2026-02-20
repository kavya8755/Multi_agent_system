"""
Groq LLM client for the multi-agent system.
Uses Groq's fast inference (e.g. Llama 3.3 70B) for agent reasoning.
"""
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Default to a capable model; switch to llama-3.1-8b-instant for speed
DEFAULT_MODEL = "llama-3.3-70b-versatile"


def get_client() -> Groq:
    """Return a Groq client using GROQ_API_KEY from environment."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not set. Create a .env file with GROQ_API_KEY=your_key"
        )
    return Groq(api_key=api_key)


def complete(
    messages: list[dict],
    model: str = DEFAULT_MODEL,
    temperature: float = 0.7,
    max_tokens: int = 2048,
) -> str:
    """
    Get a chat completion from Groq.
    messages: list of {"role": "user"|"assistant"|"system", "content": "..."}
    """
    client = get_client()
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content

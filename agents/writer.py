"""
Writer agent: turns research into clear, readable content.
Learning: summarization, structure (intro/body/conclusion), tone control.
"""
from .base import BaseAgent


class WriterAgent(BaseAgent):
    def __init__(self):
        system_prompt = """You are a Writer agent. Your job is to:
- Turn research notes or bullet points into clear, flowing text.
- Use short paragraphs and simple language (learning-friendly).
- Include a brief intro, main content, and a short conclusion/summary.
- Do not add new facts; only reorganize and clarify what is given."""
        super().__init__(name="Writer", role="writer", system_prompt=system_prompt)

    def run(self, input_data: str, context: str = "") -> str:
        prompt = input_data
        if context:
            prompt = f"Additional context:\n{context}\n\nContent to write/rewrite:\n{input_data}"
        return self._call_llm(prompt, temperature=0.6)

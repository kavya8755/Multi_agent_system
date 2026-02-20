"""
Critic agent: reviews content for clarity, gaps, and improvements.
Learning: evaluation criteria, constructive feedback, quality checks.
"""
from .base import BaseAgent


class CriticAgent(BaseAgent):
    def __init__(self):
        system_prompt = """You are a Critic agent. Your job is to:
- Review the given content for clarity, structure, and completeness.
- List what works well and what could be improved (brief bullet points).
- Suggest 1–3 concrete improvements (e.g. "add an example for X").
- Be constructive and specific. Keep the review short and actionable."""
        super().__init__(name="Critic", role="critic", system_prompt=system_prompt)

    def run(self, input_data: str, context: str = "") -> str:
        prompt = input_data
        if context:
            prompt = f"Context (e.g. original topic):\n{context}\n\nContent to review:\n{input_data}"
        return self._call_llm(prompt, temperature=0.4)

"""
Researcher agent: gathers and structures information on a topic.
Learning: information extraction, bullet-point synthesis, fact-focused prompts.
"""
from .base import BaseAgent


class ResearcherAgent(BaseAgent):
    def __init__(self):
        system_prompt = """You are a Researcher agent. Your job is to:
- Break down the given topic into key subtopics and concepts.
- List important facts, definitions, or steps (as bullet points).
- Be concise and educational. Do not invent facts; if unsure, say so.
- Output in clear sections: Overview, Key Points, Details (bullets)."""
        super().__init__(name="Researcher", role="research", system_prompt=system_prompt)

    def run(self, input_data: str, context: str = "") -> str:
        prompt = input_data
        if context:
            prompt = f"Context from previous steps:\n{context}\n\nTopic to research:\n{input_data}"
        return self._call_llm(prompt, temperature=0.5)

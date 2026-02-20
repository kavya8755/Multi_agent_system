"""
Coordinator agent: decides next step and summarizes the pipeline.
Learning: orchestration logic, state summary, simple task routing.
"""
from .base import BaseAgent


class CoordinatorAgent(BaseAgent):
    def __init__(self):
        system_prompt = """You are a Coordinator agent. Your job is to:
- Given the current pipeline state (topic, research, draft, critique), summarize what has been done.
- If asked "what next?", suggest the next logical step (e.g. "revise draft using critique" or "done").
- Keep responses very short: 1–3 sentences. Be direct and action-oriented."""
        super().__init__(name="Coordinator", role="coordinator", system_prompt=system_prompt)

    def run(self, input_data: str, context: str = "") -> str:
        prompt = input_data
        if context:
            prompt = f"Pipeline state:\n{context}\n\nRequest or question:\n{input_data}"
        return self._call_llm(prompt, temperature=0.3)

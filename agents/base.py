"""
Base agent class. All specialized agents inherit from this.
Demonstrates: single responsibility, shared LLM interface, message history.
"""
from abc import ABC, abstractmethod
from typing import Any

from llm.groq_client import complete


class BaseAgent(ABC):
    """Abstract base for all agents. Handles LLM calls and role prompt."""

    def __init__(self, name: str, role: str, system_prompt: str):
        self.name = name
        self.role = role
        self.system_prompt = system_prompt
        self._message_history: list[dict] = []

    def _messages(self, user_content: str) -> list[dict]:
        """Build message list: system + history + new user message."""
        out = [{"role": "system", "content": self.system_prompt}]
        out.extend(self._message_history)
        out.append({"role": "user", "content": user_content})
        return out

    def _call_llm(self, user_content: str, **kwargs: Any) -> str:
        """Single LLM call; optional kwargs passed to complete()."""
        messages = self._messages(user_content)
        response = complete(messages, **kwargs)
        self._message_history.append({"role": "user", "content": user_content})
        self._message_history.append({"role": "assistant", "content": response})
        return response

    @abstractmethod
    def run(self, input_data: str, context: str = "") -> str:
        """Execute the agent's task. Override in subclasses."""
        pass

    def clear_history(self) -> None:
        """Reset conversation history for a new task."""
        self._message_history.clear()

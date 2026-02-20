"""
Orchestrator: runs the multi-agent pipeline for learning.
Flow: Research -> Write -> Critic -> (optional) Coordinator summary.
"""
from agents import ResearcherAgent, WriterAgent, CriticAgent, CoordinatorAgent
from typing import Optional


class Orchestrator:
    """
    Coordinates multiple agents in sequence.
    Each agent receives the previous output as context for the next.
    """

    def __init__(self):
        self.researcher = ResearcherAgent()
        self.writer = WriterAgent()
        self.critic = CriticAgent()
        self.coordinator = CoordinatorAgent()
        self._state: dict = {}

    def run_pipeline(
        self,
        topic: str,
        run_critic: bool = True,
        run_coordinator: bool = True,
    ) -> dict:
        """
        Execute: Research(topic) -> Write(research) -> Critic(draft) -> Coordinator(summary).
        Returns dict with keys: research, draft, critique, summary.
        """
        self._state = {"topic": topic}
        # Clear history so each run is independent
        for agent in [self.researcher, self.writer, self.critic, self.coordinator]:
            agent.clear_history()

        print(f"[Orchestrator] Topic: {topic}\n")
        # 1. Research
        print("[Researcher] Running...")
        research = self.researcher.run(topic)
        self._state["research"] = research
        print("[Researcher] Done.\n")

        # 2. Write
        print("[Writer] Running...")
        draft = self.writer.run(research, context=f"Topic: {topic}")
        self._state["draft"] = draft
        print("[Writer] Done.\n")

        critique: Optional[str] = None
        if run_critic:
            print("[Critic] Running...")
            critique = self.critic.run(draft, context=topic)
            self._state["critique"] = critique
            print("[Critic] Done.\n")

        summary: Optional[str] = None
        if run_coordinator:
            state_text = f"Topic: {topic}\nResearch done. Draft done. Critique: {critique[:200] if critique else 'N/A'}..."
            print("[Coordinator] Summarizing...")
            summary = self.coordinator.run("Summarize what was done and suggest one next step.", context=state_text)
            self._state["summary"] = summary
            print("[Coordinator] Done.\n")

        return self._state

    def get_state(self) -> dict:
        return self._state.copy()


def main() -> None:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    if not os.getenv("GROQ_API_KEY"):
        print("Set GROQ_API_KEY in .env (copy from .env.example)")
        return

    topic = "How do multi-agent systems work? (in 3–5 key ideas)"
    orch = Orchestrator()
    state = orch.run_pipeline(topic, run_critic=True, run_coordinator=True)

    print("=" * 60)
    print("FINAL OUTPUTS")
    print("=" * 60)
    print("\n--- RESEARCH ---\n")
    print(state["research"])
    print("\n--- DRAFT ---\n")
    print(state["draft"])
    print("\n--- CRITIQUE ---\n")
    print(state.get("critique", "N/A"))
    print("\n--- COORDINATOR SUMMARY ---\n")
    print(state.get("summary", "N/A"))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Multi-Agent System – Learning Demo
Run: source agentic_ai/bin/activate && python main.py
Uses Groq (Llama) for Research -> Write -> Critic -> Coordinator pipeline.
"""
import os
from dotenv import load_dotenv

load_dotenv()

def check_env():
    if not os.getenv("GROQ_API_KEY"):
        print("ERROR: GROQ_API_KEY not set.")
        print("Create a .env file with: GROQ_API_KEY=your_key")
        print("Or: export GROQ_API_KEY=your_key")
        return False
    return True


def run_demo():
    from orchestrator import Orchestrator
    topic = "How do multi-agent systems work? (3–5 key ideas for beginners)"
    print("Multi-Agent Learning Demo")
    print("=" * 50)
    orch = Orchestrator()
    state = orch.run_pipeline(topic, run_critic=True, run_coordinator=True)
    print("\n" + "=" * 50)
    print("FINAL OUTPUTS")
    print("=" * 50)
    for key in ["research", "draft", "critique", "summary"]:
        if key in state and state[key]:
            print(f"\n--- {key.upper()} ---\n")
            print(state[key])


if __name__ == "__main__":
    if not check_env():
        exit(1)
    run_demo()

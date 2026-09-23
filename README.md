# Multi-Agent System (Learning Project)

A **multi-agent system**: multiple AI agents (Researcher, Writer, Critic, Coordinator) work in sequence, powered by **Groq** (Llama 3.3 70B).

## Agenda

| Component | Concept |
|-----------|--------|
| **BaseAgent** | Shared interface, message history, single LLM call pattern |
| **ResearcherAgent** | Information extraction, bullet-point synthesis |
| **WriterAgent** | Turning notes into prose, structure (intro/body/conclusion) |
| **CriticAgent** | Evaluation, constructive feedback, quality checks |
| **CoordinatorAgent** | Orchestration, state summary, “what next?” routing |
| **Orchestrator** | Chaining agents: Research → Write → Critic → Coordinator |

## Setup

1. **Create and activate the environment**
   ```bash
   cd Multi_agent_system
   python3 -m venv agentic_ai
   source agentic_ai/bin/activate   # Windows: agentic_ai\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **API key**  
   A `.env` file with `GROQ_API_KEY` is already set for local use. For a fresh clone, copy `.env.example` to `.env` and add your key. **Do not commit `.env`.**

## Run

```bash
source agentic_ai/bin/activate
python main.py
```

Or run the orchestrator directly:

```bash
python orchestrator.py
```

## Project Layout

```
Multi_agent_system/
├── agentic_ai/          # Python venv (create with python3 -m venv agentic_ai)
├── agents/
│   ├── base.py          # BaseAgent (LLM + history)
│   ├── researcher.py    # Research agent
│   ├── writer.py        # Writer agent
│   ├── critic.py        # Critic agent
│   └── coordinator.py   # Coordinator agent
├── llm/
│   └── groq_client.py   # Groq API client
├── orchestrator.py      # Pipeline: Research → Write → Critic → Coordinator
├── main.py              # Demo entrypoint
├── requirements.txt
├── .env.example
└── README.md
```

## Customization

- **Topic**: Edit `topic` in `main.py` or `orchestrator.py`.
- **Model**: In `llm/groq_client.py`, change `DEFAULT_MODEL` (e.g. `llama-3.1-8b-instant` for speed).
- **Agents**: Add new agents in `agents/` by subclassing `BaseAgent` and implementing `run()`.

## Note on “Grok”

This project uses **Groq** (groq.com) for fast LLM inference with models like **Llama 3.3 70B**. The name “Grok” here refers to using a powerful model via Groq’s API for learning; the code is model-agnostic and only needs a valid `GROQ_API_KEY`.

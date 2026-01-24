# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

mylana is a personal finance AI agent system using CrewAI to orchestrate multiple agents for USD-to-MXN currency conversion, expense tracking, and debt elimination strategies. It runs locally with Ollama for privacy.

## Commands

```bash
# Install dependencies
uv sync

# Run the main workflow
uv run mylana

# Alternative
uv run run_crew

# Train the crew
python -m mylana.main train <n_iterations> <output_filename>

# Test the crew
python -m mylana.main test <n_iterations> <eval_llm>

# Replay a previous execution
python -m mylana.main replay <task_id>

# Run with custom trigger
python -m mylana.main run_with_trigger '{"amount": "1000", "currency": "USD"}'
```

## Architecture

### Multi-Agent Sequential Workflow

The system uses three agents that execute sequentially, with each task's output passed as context to the next:

```
User Input (AMOUNT in .env)
    |
    v
[1] Currency Reporter Agent
    - Tool: ExchangeRateTool (calls exchangerate-api.com with frankfurter.app fallback)
    - Output: Exchange rate + converted MXN amount
    |
    v
[2] Personal Finance Manager Agent
    - Tool: FinanceJSONTool (reads db/expenses.json)
    - Context: Currency reporter output
    - Output: Expense breakdown + remaining balance
    - Writes: outputs/output.md
    |
    v
[3] Debt Elimination Strategist Agent
    - Tool: FinanceJSONTool
    - Context: Finance manager output
    - Output: Snowball/Avalanche analysis + payment roadmap
    - Writes: outputs/debt_strategy.md
```

### Key Components

- **`src/mylana/crew.py`**: CrewAI crew definition with `@agent`, `@task`, and `@crew` decorators. The `CurrencyAuditCrew` class orchestrates all agents.
- **`src/mylana/config/agents.yaml`**: Agent roles, goals, and backstories
- **`src/mylana/config/tasks.yaml`**: Task descriptions with `{amount_received}` and `{currency}` placeholders
- **`src/mylana/tools/`**: Custom CrewAI tools inheriting from `BaseTool` with Pydantic input schemas

### Data Flow

- Financial data stored in `db/expenses.json` (gitignored) with three categories:
  - `fixed_expenses`: Monthly bills (uses `amount` field)
  - `credit_cards`: Card balances (uses `balance` and `interest_rate` fields)
  - `debts`: Loans (uses `total_remaining` and `monthly_payment` fields)
- All amounts are in MXN

## Environment Variables

Required in `.env`:
```
AMOUNT=3000                              # USD amount to convert
LLM=ollama/gemma3:27b                    # Any Ollama model
BASE_OLLAMA_URL=http://localhost:11434   # Ollama server URL
```

## Configuration

- **Agents**: Modify `src/mylana/config/agents.yaml` for agent behavior
- **Tasks**: Modify `src/mylana/config/tasks.yaml` for task definitions
- **LLM settings**: In `crew.py`, the LLM uses `temperature=0.1` and custom stop sequences

## Dependencies

Uses `uv` package manager. Key dependencies: `crewai[tools]`, `litellm[proxy]`, `langchain-community`, `python-dotenv`, `requests`.

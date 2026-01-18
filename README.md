# mylana

A personal finance AI agent system powered by CrewAI that helps audit currency exchange rates and analyze financial transactions.

## 📋 Overview

mylana is an intelligent agent system designed to help manage personal finances, specifically focused on USD to MXN currency exchange rate monitoring. It uses CrewAI to orchestrate AI agents that can search for current exchange rates, analyze transaction costs, and provide detailed financial insights.

## ✨ Features

- **Real-time Exchange Rate Monitoring**: Automatically fetches current USD to MXN exchange rates
- **Currency Audit Agent**: Intelligent agent that searches and reports exchange rate data
- **Web Search Integration**: Uses DuckDuckGo to find the latest market rates
- **Local LLM Support**: Powered by DeepSeek R1 via Ollama for privacy and cost efficiency
- **Flexible Execution**: Run, train, test, and replay crew executions
- **Trigger-based Workflows**: Support for event-driven financial analysis

## 🚀 Installation

### Prerequisites

- Python 3.12 or 3.13
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- [Ollama](https://ollama.ai/) with DeepSeek R1 model installed

### Setup

1. Clone the repository:
```bash
git clone https://github.com/roberjacobo/mylana.git
cd mylana
```

2. Install dependencies:
```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -e .
```

3. Set up environment variables:
Create a `.env` file in the root directory with your configuration:
```bash
# Add any required API keys or configuration
```

4. Ensure Ollama is running with a valid model:
```bash
ollama pull <your-model>
ollama list
```

## 💻 Usage

### Basic Usage

Run the currency audit crew:
```bash
mylana
# or
run_crew
```

This will analyze a payment of $3000 USD and provide the current exchange rate information.

### Advanced Usage

#### Train the Crew
Train the agent system with custom iterations:
```bash
python -m mylana.main train <n_iterations> <output_filename>
```

#### Test the Crew
Test the crew with evaluation:
```bash
python -m mylana.main test <n_iterations> <eval_llm>
```

#### Replay Execution
Replay a previous crew execution:
```bash
python -m mylana.main replay <task_id>
```

#### Run with Custom Trigger
Execute with a custom JSON payload:
```bash
python -m mylana.main run_with_trigger '{"amount": "5000", "currency": "USD"}'
```

## 📁 Project Structure

```
mylana/
├── src/
│   └── mylana/
│       ├── config/
│       │   ├── agents.yaml      # Agent definitions
│       │   └── tasks.yaml       # Task configurations
│       ├── tools/
│       │   └── duckduckGoSearch_tool.py
│       ├── crew.py              # CrewAI crew definition
│       └── main.py              # Entry points
├── knowledge/                   # Knowledge base files
├── tests/                       # Test files
├── pyproject.toml              # Project dependencies
└── README.md                   # This file
```

## 🤖 How It Works

1. **Agent**: The `currency_reporter` agent is an exchange rate specialist that searches for current USD to MXN rates
2. **Task**: The `get_rate_task` instructs the agent to:
   - Search for "1 USD to MXN rate"
   - Extract the numeric exchange rate
   - Report the date and rate found
3. **Execution**: The crew processes the task sequentially and returns formatted results

## 🛠️ Technology Stack

- **CrewAI**: AI agent orchestration framework
- **LiteLLM**: LLM proxy for model flexibility
- **Ollama**: Local LLM runtime (DeepSeek R1)
- **LangChain**: Additional AI tooling
- **FastAPI**: API framework (for future extensions)
- **DuckDuckGo Search**: Web search capabilities

## 📝 Configuration

### Modifying Agents

Edit `src/mylana/config/agents.yaml` to customize agent behavior, roles, and goals.

### Modifying Tasks

Edit `src/mylana/config/tasks.yaml` to adjust task descriptions and expected outputs.

### Changing LLM

Update the LLM configuration in `src/mylana/crew.py`:
```python
deepseek = LLM(model="ollama/your-model:tag", base_url="http://localhost:11434")
```

## 🤝 Contributing

This is a personal project, but suggestions and improvements are welcome! Feel free to open issues or submit pull requests.

## 📄 License

See the [LICENSE](LICENSE) file for details.

## 🔮 Future Enhancements

- [ ] Multi-currency support beyond USD/MXN
- [ ] Historical rate tracking and visualization
- [ ] Bank fee comparison agents
- [ ] Transaction categorization and budgeting
- [ ] Web interface for easy interaction
- [ ] Automated alerts for favorable exchange rates

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Note**: This project uses local LLMs via Ollama for privacy and cost efficiency. Make sure Ollama is running before executing the crew.

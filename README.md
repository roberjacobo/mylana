# mylana

A personal finance AI agent system powered by CrewAI that helps with currency conversions, expense tracking, and financial balance calculations.

## 📋 Overview

mylana is an intelligent multi-agent system designed to help manage personal finances for USD to MXN transactions. It uses CrewAI to orchestrate AI agents that fetch real-time exchange rates, track expenses, and calculate your remaining balance after all financial obligations.

## ✨ Features

- **Real-time Currency Conversion**: Automatically fetches current USD to MXN exchange rates via API
- **Expense Tracking**: Manages fixed expenses, credit card payments, and debt obligations
- **Balance Calculator**: Calculates remaining balance after converting USD income and subtracting all expenses
- **Multi-Agent System**: Two specialized agents working sequentially
- **Local LLM Support**: Powered by Ollama for privacy and cost efficiency
- **Financial Data Management**: JSON-based storage for expenses, credit cards, and debts
- **Secure by Default**: Financial data is gitignored to protect sensitive information

## 🤖 AI Agents

### 1. Currency Exchange Rate Analyst
- Fetches real-time USD to MXN exchange rates
- Converts USD payments to Mexican Pesos
- Provides accurate conversion with timestamps

### 2. Personal Finance Manager
- Reads financial data from local database
- Calculates total monthly obligations
- Computes remaining balance after expenses

## 🚀 Installation

### Prerequisites

- Python 3.12 or 3.13
- [uv](https://github.com/astral-sh/uv) package manager
- [Ollama](https://ollama.ai/) with a compatible model installed

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mylana.git
cd mylana
```

2. Install dependencies:
```bash
uv sync
```

3. Set up environment variables:
Create a `.env` file in the root directory:
```bash
AMOUNT=1000
LLM=ollama/deepseek-r1:latest
BASE_OLLAMA_URL=http://localhost:11434
```

4. Set up your financial database:
```bash
# Copy the example file
cp db/expenses.example.json db/expenses.json

# Edit with your actual financial data
nano db/expenses.json
```

5. Ensure Ollama is running:
```bash
ollama pull deepseek-r1:latest
ollama serve
```

## 💻 Usage

### Basic Usage

Run the financial analysis:
```bash
uv run mylana
```

This will:
1. Convert your USD payment to MXN using current exchange rates
2. Load your expenses from the database
3. Calculate your remaining balance after all obligations

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
python -m mylana.main run_with_trigger '{"amount": "1000", "currency": "USD"}'
```

## 📁 Project Structure

```
mylana/
├── db/
│   ├── expenses.example.json   # Sample data structure
│   ├── expenses.json           # Your data (gitignored)
│   └── README.md               # Database documentation
├── src/
│   └── mylana/
│       ├── config/
│       │   ├── agents.yaml     # Agent definitions
│       │   └── tasks.yaml      # Task configurations
│       ├── tools/
│       │   ├── exchange_rate_tool.py      # Currency API
│       │   ├── finance_data_loader.py     # Expense loader
│       │   └── duckduckGoSearch_tool.py   # Web search
│       ├── crew.py             # CrewAI crew definition
│       └── main.py             # Entry points
├── knowledge/                  # AI knowledge base
├── tests/                      # Test files
├── .env                        # Environment variables (gitignored)
├── .gitignore                  # Git ignore rules
├── pyproject.toml              # Project dependencies
└── README.md                   # This file
```

## 🔄 Workflow

```
1. User Input (AMOUNT in .env)
   ↓
2. Currency Exchange Rate Analyst
   - Fetches USD to MXN rate
   - Converts amount to MXN
   ↓
3. Personal Finance Manager
   - Loads expenses from db/expenses.json
   - Calculates total obligations
   - Computes remaining balance
   ↓
4. Final Report
   - Exchange rate and converted amount
   - Breakdown of all expenses
   - Remaining balance
```

## 📊 Financial Data Structure

The system tracks three categories of financial obligations:

### Fixed Expenses
- Rent/Mortgage
- Utilities (electricity, water, internet, phone)
- Subscriptions (gym, streaming services)

### Credit Cards
- Card balances
- Minimum payments
- Interest rates
- Due dates

### Debts
- Loans (car, personal, student)
- Monthly payments
- Remaining months
- Interest rates

See `db/README.md` for detailed schema documentation.

## 🛠️ Technology Stack

- **CrewAI**: Multi-agent orchestration framework
- **Ollama**: Local LLM runtime
- **LiteLLM**: LLM proxy for flexibility
- **Requests**: HTTP client for exchange rate API
- **Python-dotenv**: Environment variable management
- **Pydantic**: Data validation
- **DuckDuckGo Search**: Backup web search (optional)

## 📝 Configuration

### Environment Variables (.env)

```bash
AMOUNT=1000                                    # USD amount to convert
LLM=ollama/deepseek-r1:latest                 # LLM model
BASE_OLLAMA_URL=http://localhost:11434        # Ollama server URL
```

### Modifying Agents

Edit `src/mylana/config/agents.yaml` to customize:
- Agent roles and goals
- Backstories and behavior
- Instructions and constraints

### Modifying Tasks

Edit `src/mylana/config/tasks.yaml` to adjust:
- Task descriptions
- Expected outputs
- Agent assignments

### Changing LLM

Update the `.env` file with your preferred model:
```bash
LLM=ollama/your-model:tag
```

Supported models: Any Ollama-compatible model

## 🔒 Security

- **Environment Variables**: `.env` file is gitignored
- **Financial Data**: `db/expenses.json` is gitignored
- **Example Data Only**: Only template files are tracked in git
- **Local Processing**: All data stays on your machine
- **No Cloud APIs**: Optional - uses local LLM via Ollama

## 🧪 Testing

Test the exchange rate tool:
```bash
uv run python test_exchange_rate.py
```

This validates:
- API connectivity
- Currency conversion accuracy
- Tool functionality

## 🤝 Contributing

This is a personal project, but suggestions and improvements are welcome! Feel free to open issues or submit pull requests.

## 📄 License

See the [LICENSE](LICENSE) file for details.

## 🔮 Future Enhancements

- [ ] Historical expense tracking and trends
- [ ] Budget recommendations based on spending patterns
- [ ] Multi-currency support beyond USD/MXN
- [ ] Export reports to PDF/CSV
- [ ] Web interface for easy interaction
- [ ] Alert system for low balance warnings
- [ ] Integration with bank APIs
- [ ] Savings goal tracking
- [ ] Investment portfolio analysis
- [ ] SQLite database migration

## 📚 Documentation

- [Database Structure](db/README.md) - Financial data schema
- [Implementation Notes](IMPLEMENTATION_NOTES.md) - Technical details
- [Example Data](db/expenses.example.json) - Sample expense structure

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Note**: This project uses local LLMs via Ollama for complete privacy. Your financial data never leaves your machine.

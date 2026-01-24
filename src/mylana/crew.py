import os

from crewai import Agent, Crew, Process, Task
from crewai.llm import LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv

# Tools
from mylana.tools.exchange_rate_tool import ExchangeRateTool
from mylana.tools.finance_data_loader import FinanceJSONTool

load_dotenv()

llm_model = os.getenv("LLM")
base_url = os.getenv("BASE_OLLAMA_URL")

if not llm_model or not base_url:
    raise ValueError("Missing required environmet variables: llm_model or base_url")

llm = LLM(
    model=llm_model,
    base_url=base_url,
    temperature=0.1,
    stop=["Observation:", "Tool Output:"],
)


@CrewBase
class CurrencyAuditCrew:
    """Crew for auditing USD/MXN exchange rates and payments"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def currency_reporter(self) -> Agent:
        """Expert in currency exchange and banking fees"""
        return Agent(
            config=self.agents_config["currency_reporter"],  # type: ignore
            verbose=True,
            llm=llm,
            tools=[ExchangeRateTool()],
        )

    @agent
    def personal_finance_manager(self) -> Agent:
        """Agent responsible for managing expenses and the final balance"""
        return Agent(
            config=self.agents_config["personal_finance_manager"],  # type: ignore
            verbose=True,
            llm=llm,
            tools=[FinanceJSONTool()],
            max_iter=5,  # Limit iterations to prevent infinite loops
            early_stopping_method="force",  # Force an answer if it gets stuck
            allow_delegation=False,  # Disable if not strictly necessary
        )

    @agent
    def debt_elimination_strategist(self) -> Agent:
        """Agent specializing in debt repayment strategies (Snowball/Avalanche)"""
        return Agent(
            config=self.agents_config["debt_elimination_strategist"],  # type: ignore
            verbose=True,
            llm=llm,
            tools=[FinanceJSONTool()],
            max_iter=5,
            early_stopping_method="force",
            allow_delegation=False,
        )

    @task
    def get_rate_task(self) -> Task:
        """Task to analyze rates and explain transaction costs"""
        return Task(
            config=self.tasks_config["get_rate_task"],  # type: ignore
        )

    @task
    def debt_settlement_task(self) -> Task:
        """Task to calculate the remaining balance after debts and fixed expenses"""
        return Task(
            config=self.tasks_config["debt_settlement_task"],  # type: ignore
            context=[self.get_rate_task()],  # type: ignore
            output_file="outputs/output.md",
        )

    @task
    def debt_analysis_and_strategy_task(self) -> Task:
        """Task to prioritize debts and generate the payment roadmap"""
        return Task(
            config=self.tasks_config["debt_analysis_and_strategy_task"],  # type: ignore
            context=[self.debt_settlement_task()],  # type: ignore
            output_file="outputs/debt_strategy.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CurrencyAuditCrew"""
        return Crew(
            agents=self.agents,  # type: ignore
            tasks=self.tasks,  # type: ignore
            process=Process.sequential,
            verbose=True,
            tracing=True,
            planning=False,
        )

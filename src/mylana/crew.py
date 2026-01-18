import os
from crewai import Agent, Crew, Process, Task
from crewai.llm import LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from mylana.tools.exchange_rate_tool import ExchangeRateTool

load_dotenv()

llm_model = os.getenv('LLM')
base_url = os.getenv('BASE_OLLAMA_URL')

if not llm_model or not base_url:
    raise ValueError("Missing required environmet variables: llm_model or base_url")

llm = LLM(model=llm_model, base_url=base_url)

@CrewBase
class CurrencyAuditCrew():
    """Crew for auditing USD/MXN exchange rates and payments"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def currency_reporter(self) -> Agent:
        """Expert in currency exchange and banking fees"""
        return Agent(
            config=self.agents_config['currency_reporter'], # type: ignore
            verbose=True,
            llm = llm,
            tools=[ExchangeRateTool()]
        )

    @task
    def get_rate_task(self) -> Task:
        """Task to analyze rates and explain transaction costs"""
        return Task(
            config=self.tasks_config['get_rate_task'], # type: ignore
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CurrencyAuditCrew"""
        return Crew(
            agents=self.agents, # type: ignore
            tasks=self.tasks,   # type: ignore
            process=Process.sequential,
            verbose=True,
            tracing=True,
            planning=False
        )

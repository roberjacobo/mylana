from crewai import Agent, Crew, Process, Task
from crewai.llm import LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List, Dict, Any
from dotenv import load_dotenv

load_dotenv()

deepseek = LLM(model="ollama/deepseek-r1:latest", base_url="http://localhost:11434")

@CrewBase
class CurrencyAuditCrew():
    """Crew for auditing USD/MXN exchange rates and payments"""

    # Define path constants to help the decorator and the linter
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def financial_analyst(self) -> Agent:
        """Expert in currency exchange and banking fees"""
        return Agent(
            config=self.agents_config['financial_analyst'], # type: ignore
            verbose=True,
            llm = deepseek
        )

    @task
    def currency_audit_task(self) -> Task:
        """Task to analyze rates and explain transaction costs"""
        return Task(
            config=self.tasks_config['currency_audit_task'], # type: ignore
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

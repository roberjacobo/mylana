from crewai import Agent, Crew, Process, Task
from crewai.llm import LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from mylana.tools.duckduckGoSearch_tool import SearchTool

load_dotenv()

deepseek = LLM(model="ollama/deepseek-r1:latest", base_url="http://localhost:11434")

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
            llm = deepseek,
            tools=[SearchTool()]
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

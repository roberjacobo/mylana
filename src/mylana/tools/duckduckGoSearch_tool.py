from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_community.tools import DuckDuckGoSearchRun

class SearchToolInput(BaseModel):
    """Input schema for SearchTool."""
    query: str = Field(..., description="The search query to find exchange rates, news, or economic data.")

class SearchTool(BaseTool):
    name: str = "DuckDuckGo Search"
    description: str = (
        "Useful for searching the internet to find real-time information, "
        "current USD/MXN exchange rates, and banking fees."
    )
    args_schema: Type[BaseModel] = SearchToolInput

    def _run(self, query: str) -> str:
        runner = DuckDuckGoSearchRun()
        return runner.run(query)

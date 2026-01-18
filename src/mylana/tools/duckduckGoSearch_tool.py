from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from duckduckgo_search import DDGS
from datetime import datetime

class SearchToolInput(BaseModel):
    """Input schema for SearchTool."""
    query: str = Field(..., description="The search query to find exchange rates, news, or economic data.")

class SearchTool(BaseTool):
    name: str = "DuckDuckGo Search"
    description: str = (
        "Useful for searching the internet to find real-time information, "
        "current USD/MXN exchange rates, and banking fees. Returns recent search results."
    )
    args_schema: Type[BaseModel] = SearchToolInput

    def _run(self, query: str) -> str:
        """
        Search DuckDuckGo and return formatted results with titles, snippets, and links.
        This provides more context and recent data for the agent to analyze.
        """
        try:
            ddgs = DDGS()
            results = ddgs.text(query, max_results=5)
            
            if not results:
                return "No results found for the query."
            
            # Format results with clear structure
            formatted_output = []
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            formatted_output.append(f"Search performed on: {current_date}\n")
            formatted_output.append(f"Query: {query}\n")
            formatted_output.append("=" * 80 + "\n")
            
            for idx, result in enumerate(results, 1):
                title = result.get('title', 'No title')
                snippet = result.get('body', 'No description')
                link = result.get('href', 'No link')
                
                formatted_output.append(f"\nResult {idx}:")
                formatted_output.append(f"Title: {title}")
                formatted_output.append(f"Snippet: {snippet}")
                formatted_output.append(f"Source: {link}")
                formatted_output.append("-" * 80)
            
            return "\n".join(formatted_output)
            
        except Exception as e:
            return f"Error performing search: {str(e)}"
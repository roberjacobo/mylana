import json
import os
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

class FinanceToolInput(BaseModel):
    """Input schema for FinanceTool."""
    category: str = Field(
        default="all",
        description="The category of expenses to retrieve: 'fixed_expenses', 'credit_cards', 'debts', or 'all'."
    )
    file_path: str = Field(
        default="db/expenses.json",
        description="The path to the JSON file containing financial data."
    )

class FinanceJSONTool(BaseTool):
    name: str = "Finance Data Manager"
    description: str = (
        "Reads financial data from db/expenses.json. "
        "Categories: 'fixed_expenses', 'credit_cards', 'debts', 'streaming_services', or 'all'. "
        "Credit cards: name, balance, interest_rate, cat (annual %), credit_limit, payment_due_date. "
        "Debts: description, total_remaining, monthly_payment. "
        "Fixed expenses/streaming: description, amount, due_date. "
        "Use for expense calculations, balance analysis, and debt prioritization strategies."
    )
    args_schema: Type[BaseModel] = FinanceToolInput

    def _run(self, category: str = "all", file_path: str = "db/expenses.json") -> str:
        """
        Reads the local JSON file and returns the requested financial information.

        Args:
            category: Specific category to fetch (default: all)
            file_path: Path to the JSON storage (default: db/expenses.json)

        Returns:
            Formatted string with the data or an error message.
        """
        if not os.path.exists(file_path):
            return f"Error: The file {file_path} was not found. Please ensure the database exists."

        try:
            with open(file_path, 'r') as f:
                data = json.load(f)

            # Filter logic
            if category != "all":
                if category in data:
                    result_data = {category: data[category]}
                else:
                    return f"Error: Category '{category}' not found. Available: {list(data.keys())}"
            else:
                result_data = data

            # Format output for the agent
            output = [
                "=" * 80,
                f"FINANCIAL DATA REPORT - CATEGORY: {category.upper()}",
                "=" * 80,
                json.dumps(result_data, indent=4),
                "=" * 80,
                f"Status: Data successfully retrieved from {file_path}",
                "=" * 80
            ]

            return "\n".join(output)

        except json.JSONDecodeError:
            return "Error: Failed to decode JSON. Check the file format."
        except Exception as e:
            return f"Unexpected error: {str(e)}"

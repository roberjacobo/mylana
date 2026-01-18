from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
from datetime import datetime


class ExchangeRateToolInput(BaseModel):
    """Input schema for ExchangeRateTool."""
    base_currency: str = Field(
        default="USD",
        description="The base currency code (e.g., USD, EUR, GBP)"
    )
    target_currency: str = Field(
        default="MXN",
        description="The target currency code to convert to (e.g., MXN, CAD, JPY)"
    )


class ExchangeRateTool(BaseTool):
    name: str = "Exchange Rate API"
    description: str = (
        "Gets real-time exchange rates between two currencies. "
        "Returns the current rate, timestamp, and date of the data. "
        "Useful for getting accurate USD to MXN or any other currency pair."
    )
    args_schema: Type[BaseModel] = ExchangeRateToolInput

    def _run(self, base_currency: str = "USD", target_currency: str = "MXN") -> str:
        """
        Fetch real-time exchange rate from exchangerate-api.com (free, no API key required)
        
        Args:
            base_currency: The currency to convert from (default: USD)
            target_currency: The currency to convert to (default: MXN)
            
        Returns:
            Formatted string with exchange rate, date, and additional info
        """
        try:
            # Using exchangerate-api.com free tier (no API key needed)
            url = f"https://api.exchangerate-api.com/v4/latest/{base_currency.upper()}"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract relevant information
            base = data.get('base', base_currency)
            rates = data.get('rates', {})
            date = data.get('date', 'Unknown')
            time_last_updated = data.get('time_last_updated', 'Unknown')
            
            # Get the specific rate we're looking for
            target_upper = target_currency.upper()
            if target_upper not in rates:
                return f"Error: Currency code '{target_currency}' not found. Available currencies: {', '.join(list(rates.keys())[:10])}..."
            
            rate = rates[target_upper]
            
            # Format the output
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            output = [
                "=" * 80,
                "REAL-TIME EXCHANGE RATE DATA",
                "=" * 80,
                f"Query Time: {current_datetime}",
                f"Data Last Updated: {time_last_updated}",
                f"Rate Date: {date}",
                "",
                f"Base Currency: {base}",
                f"Target Currency: {target_upper}",
                "",
                f"EXCHANGE RATE: 1 {base} = {rate} {target_upper}",
                "",
                "=" * 80,
                "Source: exchangerate-api.com",
                "=" * 80
            ]
            
            return "\n".join(output)
            
        except requests.exceptions.Timeout:
            return "Error: Request timed out. Please try again."
        except requests.exceptions.RequestException as e:
            return f"Error fetching exchange rate: {str(e)}"
        except KeyError as e:
            return f"Error parsing response data: Missing key {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"


# Alternative backup tool using a different API
class ExchangeRateToolBackup(BaseTool):
    name: str = "Exchange Rate API Backup"
    description: str = (
        "Backup tool to get real-time exchange rates if primary API fails. "
        "Uses frankfurter.app for European Central Bank data."
    )
    args_schema: Type[BaseModel] = ExchangeRateToolInput

    def _run(self, base_currency: str = "USD", target_currency: str = "MXN") -> str:
        """
        Fetch exchange rate from frankfurter.app (European Central Bank data)
        
        Args:
            base_currency: The currency to convert from (default: USD)
            target_currency: The currency to convert to (default: MXN)
            
        Returns:
            Formatted string with exchange rate information
        """
        try:
            # Using frankfurter.app (free, ECB data)
            url = f"https://api.frankfurter.app/latest?from={base_currency.upper()}&to={target_currency.upper()}"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract information
            base = data.get('base', base_currency)
            date = data.get('date', 'Unknown')
            rates = data.get('rates', {})
            
            target_upper = target_currency.upper()
            if target_upper not in rates:
                return f"Error: Currency pair {base_currency}/{target_currency} not supported by this API."
            
            rate = rates[target_upper]
            
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            output = [
                "=" * 80,
                "EXCHANGE RATE DATA (BACKUP SOURCE)",
                "=" * 80,
                f"Query Time: {current_datetime}",
                f"Rate Date: {date}",
                "",
                f"EXCHANGE RATE: 1 {base} = {rate} {target_upper}",
                "",
                "=" * 80,
                "Source: frankfurter.app (European Central Bank)",
                "=" * 80
            ]
            
            return "\n".join(output)
            
        except Exception as e:
            return f"Backup API error: {str(e)}"
import os
import sys
import warnings
from datetime import datetime
from mylana.crew import CurrencyAuditCrew
from dotenv import load_dotenv

load_dotenv()

AMOUNT = os.getenv('AMOUNT')

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew to audit a specific payment.
    """

    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

    inputs = {
        'amount_received': AMOUNT,
        'currency': 'USD',
        'current_date': formatted_date
    }

    try:
        CurrencyAuditCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'amount_received': '1000',
        'currency': 'USD',
        'current_year': str(datetime.now().year)
    }
    try:
        CurrencyAuditCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CurrencyAuditCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'amount_received': '1000',
        'currency': 'USD',
        'current_year': str(datetime.now().year)
    }

    try:
        CurrencyAuditCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "amount_received": trigger_payload.get("amount", "0"),
        "currency": "USD",
        "current_year": str(datetime.now().year)
    }

    try:
        result = CurrencyAuditCrew().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")

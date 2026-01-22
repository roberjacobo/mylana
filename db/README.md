# Database Directory

This directory contains financial data for the personal finance management system.

## File Structure

```
db/
├── README.md                  # This file
└── db/expenses.json           # Your actual data (ignored by git)
```

## Setup

1. Copy the example file to create your own data file:
   ```bash
   cp db/expenses.example.json db/expenses.json
   ```

2. Edit `db/expenses.json` with your actual financial data

3. The `expenses.json` file is automatically ignored by git to protect your sensitive financial information

## Data Structure

The JSON file contains three main categories:

### 1. Fixed Expenses
Monthly recurring expenses that don't change much:
- Rent/Mortgage
- Utilities (electricity, water, internet, phone)
- Subscriptions (gym, streaming services, etc.)

**Structure:**
```json
{
  "name": "Expense Name",
  "amount": 0.00,
  "due_date": "DD",
  "category": "housing|utilities|subscriptions"
}
```

**Example:**
```json
{
  "fixed_expenses": [
    {
      "name": "Apartment Rent",
      "amount": 8500.00,
      "due_date": "01",
      "category": "housing"
    },
    {
      "name": "Internet Service",
      "amount": 650.00,
      "due_date": "15",
      "category": "utilities"
    },
    {
      "name": "Gym Membership",
      "amount": 450.00,
      "due_date": "20",
      "category": "subscriptions"
    }
  ]
}
```

### 2. Credit Cards
Credit card balances and minimum payments:

**Structure:**
```json
{
  "name": "Card Name",
  "balance": 0.00,
  "minimum_payment": 0.00,
  "interest_rate": 0.0,
  "due_date": "DD",
  "bank": "Bank Name"
}
```

**Example:**
```json
{
  "credit_cards": [
    {
      "name": "Visa Classic",
      "balance": 12500.00,
      "minimum_payment": 375.00,
      "interest_rate": 0.24,
      "due_date": "25",
      "bank": "Banco Ejemplo"
    },
    {
      "name": "MasterCard Gold",
      "balance": 8750.00,
      "minimum_payment": 262.50,
      "interest_rate": 0.28,
      "due_date": "10",
      "bank": "Banco Nacional"
    }
  ]
}
```

### 3. Debts
Long-term debts and loans:

**Structure:**
```json
{
  "name": "Loan Name",
  "total_debt": 0.00,
  "monthly_payment": 0.00,
  "remaining_months": 0,
  "interest_rate": 0.0,
  "due_date": "DD",
  "creditor": "Creditor Name"
}
```

**Example:**
```json
{
  "debts": [
    {
      "name": "Car Loan",
      "total_debt": 185000.00,
      "monthly_payment": 3850.00,
      "remaining_months": 48,
      "interest_rate": 0.12,
      "due_date": "05",
      "creditor": "Auto Finance SA"
    },
    {
      "name": "Personal Loan",
      "total_debt": 45000.00,
      "monthly_payment": 2250.00,
      "remaining_months": 20,
      "interest_rate": 0.18,
      "due_date": "12",
      "creditor": "Banco Personal"
    }
  ]
}
```

## Complete File Example

Here's what a complete `expenses.json` file would look like:

```json
{
  "fixed_expenses": [
    {
      "name": "Apartment Rent",
      "amount": 8500.00,
      "due_date": "01",
      "category": "housing"
    },
    {
      "name": "Internet Service",
      "amount": 650.00,
      "due_date": "15",
      "category": "utilities"
    }
  ],
  "credit_cards": [
    {
      "name": "Visa Classic",
      "balance": 12500.00,
      "minimum_payment": 375.00,
      "interest_rate": 0.24,
      "due_date": "25",
      "bank": "Banco Ejemplo"
    }
  ],
  "debts": [
    {
      "name": "Car Loan",
      "total_debt": 185000.00,
      "monthly_payment": 3850.00,
      "remaining_months": 48,
      "interest_rate": 0.12,
      "due_date": "05",
      "creditor": "Auto Finance SA"
    }
  ]
}
```

## Usage

The `FinanceJSONTool` reads this file to calculate your monthly financial obligations. The agent will:

1. Read all categories or filter by specific category
2. Sum up the amounts (using `amount` for fixed expenses, `minimum_payment` for credit cards, and `monthly_payment` for debts)
3. Calculate your remaining balance after expenses

## Security Notes

⚠️ **IMPORTANT**: 
- Never commit `expenses.json` to version control
- Keep your actual financial data private
- Only use `expenses.example.json` as a template
- All amounts are in MXN (Mexican Pesos)

## Amounts

All monetary values should be in **Mexican Pesos (MXN)**.

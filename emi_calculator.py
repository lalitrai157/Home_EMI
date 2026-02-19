"""Home EMI (Equated Monthly Installment) Calculator.

Calculates the monthly EMI for a home loan based on principal amount,
annual interest rate, and loan tenure.
"""


def calculate_emi(principal, annual_rate, tenure_years):
    """Calculate the Equated Monthly Installment (EMI) for a home loan.

    Args:
        principal: Loan principal amount.
        annual_rate: Annual interest rate (in percentage, e.g. 8.5 for 8.5%).
        tenure_years: Loan tenure in years.

    Returns:
        Monthly EMI amount rounded to 2 decimal places.

    Raises:
        ValueError: If any input is non-positive, or if annual_rate is >= 100.
    """
    if principal <= 0:
        raise ValueError("Principal amount must be positive")
    if annual_rate < 0:
        raise ValueError("Annual interest rate must be non-negative")
    if tenure_years <= 0:
        raise ValueError("Loan tenure must be positive")

    if annual_rate == 0:
        return round(principal / (tenure_years * 12), 2)

    monthly_rate = annual_rate / (12 * 100)
    num_months = tenure_years * 12

    emi = principal * monthly_rate * ((1 + monthly_rate) ** num_months) / (
        ((1 + monthly_rate) ** num_months) - 1
    )
    return round(emi, 2)


def main():
    """Interactive CLI for the Home EMI calculator."""
    print("=== Home EMI Calculator ===")
    try:
        principal = float(input("Enter loan principal amount: "))
        annual_rate = float(input("Enter annual interest rate (%): "))
        tenure_years = int(input("Enter loan tenure (years): "))

        emi = calculate_emi(principal, annual_rate, tenure_years)
        total_payment = round(emi * tenure_years * 12, 2)
        total_interest = round(total_payment - principal, 2)

        print(f"\nMonthly EMI: {emi}")
        print(f"Total Payment: {total_payment}")
        print(f"Total Interest: {total_interest}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

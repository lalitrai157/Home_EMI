def calculate_emi(principal, annual_rate, tenure_months):
    """
    Calculate EMI (Equated Monthly Installment) for a home loan.

    Parameters:
        principal (float): Loan amount in currency units
        annual_rate (float): Annual interest rate in percentage (e.g., 8.5 for 8.5%)
        tenure_months (int): Loan tenure in months

    Returns:
        float: Monthly EMI amount
    """
    monthly_rate = annual_rate / (12 * 100)

    if monthly_rate == 0:
        return principal / tenure_months

    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / \
          ((1 + monthly_rate) ** tenure_months - 1)
    return round(emi, 2)


def calculate_total_payment(emi, tenure_months):
    """Return total amount paid over the loan tenure."""
    return round(emi * tenure_months, 2)


def calculate_total_interest(principal, total_payment):
    """Return total interest paid over the loan tenure."""
    return round(total_payment - principal, 2)


def main():
    print("=== Home Loan EMI Calculator ===\n")

    principal = float(input("Enter loan amount (₹): "))
    annual_rate = float(input("Enter annual interest rate (%): "))
    tenure_years = float(input("Enter loan tenure (years): "))

    tenure_months = int(tenure_years * 12)

    emi = calculate_emi(principal, annual_rate, tenure_months)
    total_payment = calculate_total_payment(emi, tenure_months)
    total_interest = calculate_total_interest(principal, total_payment)

    print(f"\n--- Results ---")
    print(f"Monthly EMI:      ₹{emi:,.2f}")
    print(f"Total Payment:    ₹{total_payment:,.2f}")
    print(f"Total Interest:   ₹{total_interest:,.2f}")


if __name__ == "__main__":
    main()

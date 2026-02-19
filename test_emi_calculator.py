from emi_calculator import calculate_emi, calculate_total_payment, calculate_total_interest


def test_calculate_emi_standard():
    emi = calculate_emi(1000000, 8.5, 240)
    assert emi == 8678.23


def test_calculate_emi_zero_rate():
    emi = calculate_emi(120000, 0, 12)
    assert emi == 10000.0


def test_calculate_total_payment():
    emi = 8678.23
    total = calculate_total_payment(emi, 240)
    assert total == 2082775.2


def test_calculate_total_interest():
    total_interest = calculate_total_interest(1000000, 2082775.2)
    assert total_interest == 1082775.2

"""Tests for the Home EMI Calculator."""

import unittest

from emi_calculator import calculate_emi


class TestCalculateEMI(unittest.TestCase):
    """Test cases for the calculate_emi function."""

    def test_standard_loan(self):
        """Test EMI calculation for a typical home loan."""
        # 10,00,000 at 8.5% for 20 years
        emi = calculate_emi(1000000, 8.5, 20)
        self.assertAlmostEqual(emi, 8678.23, places=2)

    def test_zero_interest_rate(self):
        """Test EMI with zero interest rate."""
        emi = calculate_emi(120000, 0, 10)
        self.assertEqual(emi, 1000.0)

    def test_short_tenure(self):
        """Test EMI for a 1-year loan."""
        emi = calculate_emi(120000, 12, 1)
        self.assertAlmostEqual(emi, 10661.85, places=2)

    def test_negative_principal_raises(self):
        """Test that negative principal raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_emi(-100000, 8.5, 20)

    def test_zero_principal_raises(self):
        """Test that zero principal raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_emi(0, 8.5, 20)

    def test_negative_rate_raises(self):
        """Test that negative interest rate raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_emi(100000, -5, 20)

    def test_zero_tenure_raises(self):
        """Test that zero tenure raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_emi(100000, 8.5, 0)

    def test_negative_tenure_raises(self):
        """Test that negative tenure raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_emi(100000, 8.5, -5)


if __name__ == "__main__":
    unittest.main()

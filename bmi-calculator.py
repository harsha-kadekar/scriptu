#!/usr/bin/env python3
"""Command-line BMI (Body Mass Index) calculator.

Usage:
    python3 bmi-calculator.py <weight_in_kgs> [height_in_centimeters]
"""
import argparse


def get_bmi(weight: float, height_cms: float) -> float:
    """Calculate Body Mass Index.

    Args:
        weight: Weight in kilograms.
        height_cms: Height in centimeters.

    Returns:
        BMI as weight_kg / height_m ** 2.
    """
    height_mtrs = height_cms/100
    return weight/(height_mtrs*height_mtrs)

def main():
    """Parse CLI arguments and print the calculated BMI."""
    parser = argparse.ArgumentParser(description="BMI Calculator")
    parser.add_argument("weight_in_kgs", help="weight of person in kgs", type=float)
    # 161.29 cm (~5'3") is used as a fallback height when none is provided
    parser.add_argument("height_in_centimeters", nargs="?", help="height in centimeters", default=161.29, type=float)

    args = parser.parse_args()

    print(f"Weight={args.weight_in_kgs}, Height={args.height_in_centimeters}")
    bmi = get_bmi(args.weight_in_kgs, args.height_in_centimeters)
    print(f"BMI is {bmi}")

if __name__ == "__main__":
    main()



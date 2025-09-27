#!/usr/bin/env python3

# HTB Coding Challenge "Addition" - Solution by HollowDragonX
# https://www.github.com/HollowDragonX/htb-challenges

def add_numbers(num1: int, num2: int) -> int:
    """
        Adds two numbers together.
        
    Args:
        num1 (int): First number to add.
        num2 (int): Second number to add.

    Returns:
        int: The sum of num1 and num2.
    """
    
    return num1 + num2


def main() -> None:
    
    num1 = int(input())
    num2 = int(input())

    print(add_numbers(num1, num2))


if __name__ == "__main__":
    main()
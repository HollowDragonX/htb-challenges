#!/usr/bin/env python3

# HTB Coding Challenge "Reversal" - Solution by HollowDragonX
# https://www.github.com/HollowDragonX/htb-challenges

def reverse_string(string: str) -> str:
    """
        Reverses the given string.
    
    Args:
        string (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    
    return string[::-1]


def main() -> None:
    
    string = input()

    print(reverse_string(string))


if __name__ == "__main__":
    main()
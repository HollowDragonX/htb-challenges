# Oddly Even

The ghostly clock ticks strangely. Determine whether its chimes are even or odd to calm the restless spirits.

---

## :material-text-box: Challenge description

Take in a number, print "odd" if odd and "even" if even.

```
Input:
3
```

```
Output:
odd
```


---

## :material-language-python: Solution script

```python
#!/usr/bin/env python3

# HTB Coding Challenge "Oddly Even" - Solution by HollowDragonX
# https://www.github.com/HollowDragonX/htb-challenges

def check_parity(number: int) -> bool:
    """
        Checks if the recieved number is odd or even.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, False if odd.
    """
    
    return number % 2 == 0


def get_parity_message(number: int) -> str:
    """
        Returns a message indicating if the number is odd or even.

    Args:
        number (int): The number to check.

    Returns:
        str: "even" if the number is even, "odd" if odd.
    """
    
    if check_parity(number):
        return "even"
    else:
        return "odd"
    

def main() -> None:
    
    number = int(input())

    print(get_parity_message(number))


if __name__ == "__main__":
    main()
```
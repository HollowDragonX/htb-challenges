# Reversal

A dark incantation was written backward in a spellbook. Reverse the cursed words to reveal their true meaning.

---

## :material-text-box: Challenge description

 Take in a string. Print the reverse. 

```
Input: 
Test me
```

```
Output:
em tseT
```

---

## :material-language-python: Solution script

```python
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
```
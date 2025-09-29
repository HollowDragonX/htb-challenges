# MinMax

In a haunted graveyard, spirits hide among the numbers. Can you identify the smallest and largest among them before they vanish?

---

## :material-text-box: Challenge description

 We've intercepted codes from an underground organisation with intentions of malicious activity. Intelligence has informed us that most of the numbers are garbage, but the biggest and smallest numbers in the file form co-ordinates of the group's next attack location.

Identify these 2 numbers, then print out first the minimum and then the maximum. Please be swift, agent - the clock is ticking! 

```
Input:
3.29 3.09 1.34 2.89 
```

```
Output:
1.34
3.29
```

---

## :material-language-python: Solution script

```python
#!/usr/bin/env python3

# HTB Coding Challenge "MinMax" - Solution by HollowDragonX
# https://www.github.com/HollowDragonX/htb-challenges


def main() -> None:
    
    codes = list(map(float, input().split()))
    
    print(min(codes))
    print(max(codes))

if __name__ == "__main__":
    main()
```
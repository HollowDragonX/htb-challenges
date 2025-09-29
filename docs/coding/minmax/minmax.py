#!/usr/bin/env python3

# HTB Coding Challenge "MinMax" - Solution by HollowDragonX
# https://www.github.com/HollowDragonX/htb-challenges


def main() -> None:
    
    codes = list(map(float, input().split()))
    
    print(min(codes))
    print(max(codes))

if __name__ == "__main__":
    main()
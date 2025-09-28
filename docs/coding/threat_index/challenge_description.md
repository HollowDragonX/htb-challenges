# Threat Index

Volnayan APTs are exfiltrating data through TOR nodes, embedding attack signals in plain sight. Your job is to scan each outbound stream and identify known malicious keywords linked to Operation Blackout. Each keyword has a threat level — the more hits you find, the higher the danger. Analyze the stream, tally the signals, and calculate the overall threat score.

---
## :material-text-box: Challenge description

You are monitoring data streams exiting suspicious TOR nodes, believed to be part of the Empire of Volnaya’s covert APT infrastructure.
As Talion “Little Byte” Reyes you’ve been assigned to identify and evaluate indicators of compromise embedded in the exfiltrated traffic.

Your job is to scan each stream for high-risk keywords associated with known attack patterns linked to Operation Blackout.

Each keyword has a weight representing its severity, based on intelligence recovered from earlier breaches.
The more often a keyword appears — and the higher its weight - the greater the threat posed by that stream.
The data stream contains only lowercase letters and digits.

You must calculate the threat score of each stream using the formula:

```python
threat score = Σ (occurrences of keyword × keyword weight)
```

Here is the list of all the keywords and their associated weight:

```python
KEYWORD      -> WEIGHT
"scan"       -> 1
"response"   -> 2
"control"    -> 3
"callback"   -> 4
"implant"    -> 5
"zombie"     -> 6
"trigger"    -> 7
"infected"   -> 8
"compromise" -> 9
"inject"     -> 10
"execute"    -> 11
"deploy"     -> 12
"malware"    -> 13
"exploit"    -> 14
"payload"    -> 15
"backdoor"   -> 16
"zeroday"    -> 17
"botnet"     -> 18
```

```
30 <= data stream length <= 10^6
```

```
Input:
payloadrandompayloadhtbzerodayrandombytesmalware
```
```
Expected output:
60
```

```
Analyzing the data stream:
payloadrandompayloadhtbzerodayrandombytesmalware
^^^^^^^      ^^^^^^^   ^^^^^^^           ^^^^^^^
  15           15        17                13

Calculating the threat score:

threat score = 2 * 15 + 17 + 13 = 60
```

---

## :material-language-python: Solution script

```python
#!/usr/bin/env python3

# HTB Coding Challenge "Threat Index" - Solution by HollowDragonX
# https://www.github.com/HollowDragonX/htb-challenges

def calculate_threat_score(data_stream: str, blacklist_keywords: dict[str, int]) -> int:
    """
    Calculates the threat score based on the occurrence of blacklist keywords in a data stream.
    
    Args:
        data_stream (str): The input data stream to analyze.
        blacklist_keywords (dict[str, int]): A dictionary mapping keywords to their threat weights.

    Returns:
        int: The calculated threat score.
    """
    
    threat_score = 0
    for keyword, weight in blacklist_keywords.items():
        occurence = data_stream.count(keyword)
        threat_score += (occurence * weight)
    return threat_score


def main() -> None:
    
    data_stream = input()

    blacklist_keywords = {
        "scan": 1,
        "response": 2,
        "control": 3,
        "callback": 4,
        "implant": 5,
        "zombie": 6,
        "trigger": 7,
        "infected": 8,
        "compromise": 9,
        "inject": 10,
        "execute": 11,
        "deploy": 12,
        "malware": 13,
        "exploit": 14,
        "payload": 15,
        "backdoor": 16,
        "zeroday": 17,
        "botnet": 18
    }

    print(calculate_threat_score(data_stream, blacklist_keywords))


if __name__ == "__main__":
    main()
```
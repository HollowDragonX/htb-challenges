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


    
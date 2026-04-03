# https://leetcode.com/problems/group-anagrams/?q=group+anagrams
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams: defaultdict[str, list[str]] = defaultdict(list)

    for chunk in strs:
        sorted_chunk = "".join(sorted(chunk))
        anagrams[sorted_chunk].append(chunk)

    return list(anagrams.values())

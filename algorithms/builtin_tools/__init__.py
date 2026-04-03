from collections import defaultdict

# Without the defaultdict we need to check if key exists
normal_dict: dict[str, int] = {}
normal_dict["key"] = normal_dict.get("key", 0) + 1

# With defaultdict same flow as above
str_defaultdict: defaultdict[str, int] = defaultdict(int) # default 0
str_defaultdict["key"] += 1

list_defaultdict: defaultdict[str, list[str]] = defaultdict(list) # default []
list_defaultdict["key"].append("value")

set_defaultdict: defaultdict[str, set[str]] = defaultdict(set)     # default set()
set_defaultdict["key"].add("value")

# Use it for: grouping, graph adjacency list, counting
edges: list[tuple[int, int]] = [(0, 0), (0, 1), (1, 0), (1, 1)]
graph: defaultdict[int, list[int]] = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

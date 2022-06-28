import itertools
import pathlib

GRAPH = {"000": ["000", "001"], "001": ["010", "011"],
         "011": ["111", "110"], "111": ["111", "110"],
         "110": ["101", "100"], "101": ["010", "011"],
         "010": ["100", "101"], "100": ["000", "001"]}

NODES = ["000", "001", "010", "011",
         "100", "101", "110", "111"]


def get_hamiltonian_path(start_node):
    results = []
    paths_list = list(itertools.permutations(NODES))
    for pathCandidate in paths_list:
        isHamiltonian = True
        for i in range(len(pathCandidate)-1):
            currentNode = pathCandidate[i]
            nextNode = pathCandidate[i+1]
            edgeList = GRAPH[currentNode]
            hasNoPathToNext = not nextNode in edgeList
            if(hasNoPathToNext):
                isHamiltonian = False
        if isHamiltonian == True:
            results.append(pathCandidate)
    return(results)


def trim_concat(string1, string2):
    k = 0
    for i in range(1, len(string2)):
        if string1.endswith(string2[:i]):
            k = i
    # Simply concatenate them
    return string1 + string2[k:]


if __name__ == "__main__":
    paths = []
    result = ""
    sequence_number = 1
    for node in NODES[0:4]:
        paths = get_hamiltonian_path(node)
        for path in paths:
            for node_string in path:
                result = trim_concat(result, node_string)
            print(f"{sequence_number}: {result}")
            result = ""
            sequence_number += 1

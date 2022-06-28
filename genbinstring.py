import itertools

# debruijn graph
GRAPH = {"000": ["000", "001"], "001": ["010", "011"],
         "011": ["111", "110"], "111": ["111", "110"],
         "110": ["101", "100"], "101": ["010", "011"],
         "010": ["100", "101"], "100": ["000", "001"]}

# nodes on GRAPH
NODES = ["000", "001", "010", "011",
         "100", "101", "110", "111"]


def get_hamiltonian_paths(start_node):
    '''
    Returns the list of Hamiltonian paths from a starting node on a directed graph

    Calculates all the permutations for all the possible potential paths
    and checks if they lead to a full traversal
    '''
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
    '''
    Concats two strings and removes all equal substrings at the place of the concat
    
    Example: trim_concat("abcd", "cdef") returns "abcdef"
    '''
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
        # save a list of all hamiltonian paths for 'node'
        paths = get_hamiltonian_paths(node)
        for path in paths:
            # append with trim the whole string after 'result'
            for node_string in path:
                result = trim_concat(result, node_string)
            # print result
            print(f"{sequence_number}: {result}")
            result = ""
            sequence_number += 1

import random


def is_consistent(graph, variable_value_pairs):
    """
        returns True if the variables that have been assigned a value so far are consistent with the constraints, 
        and False otherwise.
        
        variable_value_pairs can be used to access any value of any variable from the variable as a key
        you can use variable_value_pairs.items() to traverse it as (state, color) pairs
                    variable_value_pairs.keys() to get all the variables,         
                and variable_value_pairs.values() to get all the values
    """
    "*** YOUR CODE HERE ***"
    for var, value in variable_value_pairs.items():
        for neighbor in graph[var]:
            if variable_value_pairs[neighbor] is not None:
                if variable_value_pairs[neighbor] == value:
                    return False
    return True


def is_solved(graph, variable_value_pairs):
    """
        returns True if the CSP is solved, and False otherwise
    """
    "*** YOUR CODE HERE ***"
    if not is_consistent(graph, variable_value_pairs):
        return False

    for value in variable_value_pairs.values():
        if value is None:
            return False
    return True


def get_next_variable(variable_value_pairs, domains):
    """
        returns the index of the next variable from the default order of the unassinged variables
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(domains)):
        if variable_value_pairs[i] is None:
            return i
    return None


def get_chosen_variable(graph, variable_value_pairs, domains):
    """
        returns the next variable that is deemed the best choice by the proper heuristic
        use a second heuristic for breaking ties from the first heuristic
    """
    "*** YOUR CODE HERE ***"
    "MRV & degree heuristic"
    chosen_variable = None
    min_domain_size = float('inf')
    max_degree = -1
    for var in graph:
        if variable_value_pairs[var] is None:
            domain_size = len(domains[var])
            degree = len(graph[var])

            if domain_size < min_domain_size or (domain_size == min_domain_size and degree > max_degree):
                min_domain_size = domain_size
                max_degree = degree
                chosen_variable = var

    return chosen_variable


def get_ordered_domain(graph, domains, variable):
    """
        returns the domain of the varibale after ordering its values by the proper heuristic
        (you may use imports here)
    """
    "*** YOUR CODE HERE ***"
    value_counts = {}
    for value in domains[variable]:
        count = 0
        for neighbour in graph[variable]:
            if value in domains[neighbour]:
                count += 1
        value_counts[value] = count

    ordered_values = dict(sorted(value_counts.items(), key=lambda x: x[1]))

    return ordered_values.keys()


def forward_check(graph, variable_value_pairs, domains, variable, value):
    """
        removes the value assigned to the current variable from its neighbors
        returns True if backtracking is necessary, and False otherwise
    """
    "*** YOUR CODE HERE ***"
    for neighbor in graph[variable]:
        if variable_value_pairs[neighbor] is None:
            if value in domains[neighbor]:
                domains[neighbor].remove(value)
            if len(domains[neighbor]) == 0:
                return True
    return False


def ac3(graph, variable_value_pairs, domains):
    """
        maintains arc-consistency
        returns True if backtracking is necessary, and False otherwise
    """
    "*** YOUR CODE HERE ***"
    from collections import deque

    queue = deque((source, target) for source in graph for target in graph[source])

    while queue:
        source, target = queue.popleft()
        if revise(variable_value_pairs, domains, source, target):
            if not domains[source]:
                return True
            for neighbor in graph[source]:
                if neighbor != target:
                    queue.append((neighbor, source))

    return False


def revise(variable_value_pairs, domains, source, target):
    revised = False
    if variable_value_pairs[target] is not None:
        if variable_value_pairs[target] in domains[source]:
            domains[source].remove(variable_value_pairs[target])
            revised = True
    return revised


def random_choose_conflicted_var(graph, variable_value_pairs):
    """
        returns a random variable that is conflicting with a constrtaint
    """
    "*** YOUR CODE HERE ***"
    conflicted_vars = []
    for var in graph:
        conflict_found = False
        for neighbor in graph[var]:
            if variable_value_pairs.get(var) == variable_value_pairs.get(neighbor):
                conflict_found = True
                break

        if conflict_found:
            conflicted_vars.append(var)

    return random.choice(conflicted_vars) if conflicted_vars else None


def get_chosen_value(graph, variable_value_pairs, domains, variable):
    """
        returns the value by using the proper heuristic
        NOTE: handle tie-breaking by random
    """
    "*** YOUR CODE HERE ***"
    neighbor_var_values = {}
    for neighbor in graph[variable]:
        neighbor_var_values[neighbor] = variable_value_pairs[neighbor]

    tmp = {}
    for value in domains[variable]:
        count = 0
        for neighbor in graph[variable]:
            if neighbor_var_values.get(neighbor) == value:
                count += 1
        tmp[value] = count
    min_conflicts = dict(sorted(tmp.items(), key=lambda x: x[1]))
    min_conflict_value = list(min_conflicts.values())[0]
    chosen_var_values = {}
    for var, value in tmp.items():
        if value == min_conflict_value:
            chosen_var_values[var] = min_conflict_value

    return random.choice(list(chosen_var_values.keys()))

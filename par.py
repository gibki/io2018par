def is_periodic(chain, period_length):
    for index in range(len(chain) - period_length):
        if chain[index] != chain[index + period_length]:
            return False

    return True

def calculate_chain_parity(chain):
    return sum(chain) % 2

def best_answer_from_single_chain(chain):
    return index_to_answer(first_different_element_index(chain), len(chain))

def first_different_element_index(chain):
    first_different = len(chain)

    for index, element in enumerate(chain):
        if element != chain[0]:
            first_different = min(first_different, index, len(chain) - 1 - index)

    return first_different

def index_to_answer(index, chain_length):
    return chain_length - index - 1

def calculate_longest_subchain_length(n, m, a, b):
    if not is_periodic(a, m):
        return m

    if calculate_chain_parity(a[:m]) == calculate_chain_parity(b):
        return m

    if a[0] != b[0]:
        return m - 1

    # reduce problem space to chains where n < 2m
    n, a = min(n, 2 * m - 1), a[:2 * m - 1]

    return max(min(best_answer_from_single_chain(a), m - 1),
               best_answer_from_single_chain(b))


q = int(input())
for i in range(q):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    # reduce the problem space to chains with gems of value 0 or 1
    a = [x % 2 for x in a]
    b = [x % 2 for x in b]

    # reduce the problem space to cases where first chain if not shorter one
    if m > n:
        a, b, n, m = b, a, m, n

    print(calculate_longest_subchain_length(n, m, a, b))

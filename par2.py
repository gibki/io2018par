def is_periodic(chain, period_length):
    for index in range(len(chain) - period_length):
        if chain[index] != chain[index + period_length]:
            return False

    return True

def calculate_chain_parity(chain):
    return sum(chain) % 2

def calculate_longest_subchain_length(n, m, a, b):
    for length in reversed(range(m + 1)):
        if not is_periodic(a, length) or not is_periodic(b, length):
            return length

        if calculate_chain_parity(a[:length]) == calculate_chain_parity(b[:length]):
            return length

        n, a = min(n, 2 * length - 1), a[:2 * length - 1]
        # the following line never actually does anything, see if you can figure
        # out why
        m, b = min(m, 2 * length - 1), b[:2 * length - 1]

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

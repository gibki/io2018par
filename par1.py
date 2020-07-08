def generate_subchains(chain, length):
    subchain_count = len(chain) - length + 1
    return [chain[x:x + length] for x in range(subchain_count)]

def calculate_chain_parity(chain):
    return sum(chain) % 2

def calculate_longest_subchain_length(n, m, a, b):
    if m > n:
        n, m, a, b = m, n, b, a

    for length in reversed(range(m + 1)):
        for chain_a_subchain in generate_subchains(a, length):
            for chain_b_subchain in generate_subchains(b, length):
                if calculate_chain_parity(chain_a_subchain) ==\
                   calculate_chain_parity(chain_b_subchain):
                    return length

q = int(input())
for i in range(q):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    print(calculate_longest_subchain_length(n, m, a, b))

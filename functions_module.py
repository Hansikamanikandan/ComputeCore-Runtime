def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def prime_factors(n):
    pf = []
    i = 2
    while n > 1:
        if n % i == 0:
            pf.append(i)
            n //= i
        else:
            i += 1
    return pf

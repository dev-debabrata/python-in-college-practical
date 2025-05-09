# 13. Form two function blocks which calculate the HCF and LCM of two no.s


def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // hcf(a, b)

print("HCF:", hcf(12, 18))
print("LCM:", lcm(12, 18))

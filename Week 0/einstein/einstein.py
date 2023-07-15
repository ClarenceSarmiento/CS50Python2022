def solve(m):
    c = 300000000
    E = m * c ** 2
    return E

def main():
    m = int(input("mass: " ))
    print(solve(m))

main()
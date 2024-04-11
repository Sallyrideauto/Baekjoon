import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    while True:
        if is_prime(n):
            return n
        n += 1

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        print(next_prime(n))

if __name__ == '__main__':
    main()
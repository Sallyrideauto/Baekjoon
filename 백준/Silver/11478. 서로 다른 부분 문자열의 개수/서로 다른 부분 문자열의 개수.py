import sys

def main():
    S = sys.stdin.readline().strip()
    S_len = len(S)
    S_set = set()
    for i in range(S_len):
        for j in range(i+1, S_len+1):
            S_set.add(S[i:j])
    print(len(S_set))

if __name__ == '__main__':
    main()
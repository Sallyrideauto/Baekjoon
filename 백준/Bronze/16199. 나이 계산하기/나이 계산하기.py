# https://github.com/xCrypt0r/Baekjoon/blob/master/src/16/16199.py

def main():
    BY, BM, BD = map(int, input().split())
    NY, NM, ND = map(int, input().split())
    age = NY - BY

    print(age - (0 if BM < NM or (BM == NM and BD <= ND) else 1), age + 1, age, sep='\n')

if __name__ == '__main__':
    main()
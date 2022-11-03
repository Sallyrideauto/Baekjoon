def solution(price: int) -> int:
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    return price

if __name__ == '__main__':
    print(solution(150000))
    print(solution(580000))
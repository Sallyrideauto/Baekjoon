function solution(price, money, count) {
    
    let countprice = 0;
    
    for (let i = 1; i <= count; i++) {
        countprice += price * i;
    }
    
    return money > countprice ? 0 : countprice - money;
    
}

// https://velog.io/@ongsim123/Algorithm-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B6%80%EC%A1%B1%ED%95%9C-%EA%B8%88%EC%95%A1-%EA%B3%84%EC%82%B0%ED%95%98%EA%B8%B0-Javascript
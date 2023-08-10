process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const num = data.split(" ");
    const n = Number(num[0]), m = Number(num[1]);
    
    for (let i = 0; i < m; i++) {
        let str = "";
        for (let j = 0; j < n; j++) {
            str = str + "*";
        }
    console.log(str)    
    }
    
});

// https://hianna.tistory.com/368
// https://velog.io/@wjdaud107/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8javascript%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95-%EB%B3%84-%EC%B0%8D%EA%B8%B0
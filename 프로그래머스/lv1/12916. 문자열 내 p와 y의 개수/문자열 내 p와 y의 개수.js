function solution(s){
    let change = s.toLowerCase();
    
    let check_p = change.split("p").length;
    let check_y = change.split("y").length;
    
    return check_p === check_y ? true : false;
}
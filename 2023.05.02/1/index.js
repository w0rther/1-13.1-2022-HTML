
function vizsgal (szam, min, max) {
    return (szam >= min && szam <= max);    

}


function make_mx(szam = 5, N = 10, M = 10) {
    let mx = [];
    for (var i = 0; i < N; i++) {
        mx[i] = [];
        for (var j = 0; j < M; j++) {
            mx [i][j] = szam;
        }
    }
    return mx;
}


console.log(make_mx());


function inc_mx(mx, x, y) {
    for (let i = -1; i <= 1; i++) {
        for (let j = -1; j <= 1; j++) {
    x = x + i;
    y = y + j;
  mx[y][x] += 1;
}
    }
}

console.log(inc_mx(make_mx(1,5,5), 2,4));
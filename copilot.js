const array = [1, 2, 3, 4, 5];

const doubled = array.map(num => num * 2);

console.log(doubled);

const uniqueSet = new Set([1, 2, 2, 3, 4, 4, 5]);
console.log(uniqueSet);

const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('Promise resolved!');
    }, 1000);
});

promise.then(result => {
    console.log(result);
}).catch(error => {
    console.error(error);
});
function reverseArray(n, arr) {
    const slicedArr = arr.slice(0, n);
    const reversedArr = slicedArr.reverse();
    const result = reversedArr.join(' ');
    console.log(result);
}


reverseArray(3, [10, 20, 30, 40, 50])
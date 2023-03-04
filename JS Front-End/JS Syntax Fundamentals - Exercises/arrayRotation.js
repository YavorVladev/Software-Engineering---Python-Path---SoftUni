function rotateArray(arr, rotations) {
    const len = arr.length;
    const steps = rotations % len;
    const rotated = arr.slice(steps).concat(arr.slice(0, steps));
    return rotated.join(' ');
}

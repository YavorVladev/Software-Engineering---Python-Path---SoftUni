function cityInfo(city) {

    let tuples = Object.entries(city);

    for (const [k, v] of tuples) {
        console.log(`${k} -> ${v}`);
    }
}


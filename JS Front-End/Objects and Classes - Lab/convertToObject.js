function convertToObject(jsonFile) {

    let myObject = JSON.parse(jsonFile);

    for (const key in myObject) {
        console.log(`${key}: ${myObject[key]}`);
    }

}

convertToObject('{"name": "George", "age": 40, "town": "Sofia"}')

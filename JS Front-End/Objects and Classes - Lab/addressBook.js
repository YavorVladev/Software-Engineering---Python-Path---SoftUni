function addressBook_(data) {

    let personInfo = {};

    for (const el of data) {

        const [name, address] = el.split(":")

        if (personInfo[name]) {
            personInfo[name] = address;
        } else {
            personInfo[name] = address;
        }
    }


    const sortedKeys = Object.keys(personInfo).sort()

    sortedKeys.forEach(name => {
        console.log(`${name} -> ${personInfo[name]}`);
    })
}

addressBook_(['Tim:Doe Crossing',
'Bill:Nelson Place',
'Peter:Carlyle Ave',
'Bill:Ornery Rd']
)
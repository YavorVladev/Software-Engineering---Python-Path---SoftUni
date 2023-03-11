function phoneBook_(data) {

    let phoneBook = {};

    for (const el of data) {
        let [name, phoneNumber] = el.split(" ");
        phoneBook[name] = phoneNumber
    }

    for (const p in phoneBook) {
        console.log(`${p} -> ${phoneBook[p]}`);
    }
}

phoneBook_(['Tim 0834212554',
'Peter 0877547887',
'Bill 0896543112',
'Tim 0876566344']
)
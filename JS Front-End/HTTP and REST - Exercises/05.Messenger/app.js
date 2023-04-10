function attachEvents() {

    const BASE_URL = `http://localhost:3030/jsonstore/messenger/`;

    const inputDOMSelectors = {
        auhtorInput: document.querySelector('input[name="author"]'),
        contentInput: document.querySelector(`input[name="content"]`)

    }

    const otherDOMSelectors = {
        sendBtn: document.getElementById("submit"),
        refreshBtn: document.getElementById('refresh'),
        textAreaContainer: document.getElementById('messages')
    }


    otherDOMSelectors.refreshBtn.addEventListener('click', refreshEventHandler);
    otherDOMSelectors.sendBtn.addEventListener('click', sendEventHandler);



    async function refreshEventHandler() {

        otherDOMSelectors.textAreaContainer.textContent = "";
        let output = [];
        

        const resData = await fetch(BASE_URL);
        let workingData = await resData.json();

        
        for (const uniqueID in workingData) {
            

            const { author, content } = workingData[uniqueID];

            output.push(`${author}: ${content}`) // [ "Yavor: Hey" , "Adrean: Whatsup"]

        }

        otherDOMSelectors.textAreaContainer.textContent = output.join('\n')

    }

    function sendEventHandler() {

        let author = inputDOMSelectors.auhtorInput.value;
        let content = inputDOMSelectors.contentInput.value;


        const httpHeader = {
            method: "POST",
            body: JSON.stringify({ author, content })
        }

        fetch(BASE_URL, httpHeader)
            .then((res) => res.json())
            .then(() => {
                refreshEventHandler();

            })
    }


    
}

attachEvents();
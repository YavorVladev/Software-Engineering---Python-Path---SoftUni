function attachEvents() {

    const BASE_URL = `http://localhost:3030/jsonstore/phonebook/`;


    const inputDOMSelectors = {
        personInput: document.getElementById("person"),
        phoneInput: document.getElementById("phone")
    };

    const otherDOMSelectors = {
        loadBtn: document.getElementById("btnLoad"),
        createBtn: document.getElementById("btnCreate"),
        phoneBookContainer: document.getElementById("phonebook")
    };

    otherDOMSelectors.loadBtn.addEventListener('click', loadEventHandler);
    otherDOMSelectors.createBtn.addEventListener("click", createEventHandler);

    function createEventHandler() {

        let person = inputDOMSelectors.personInput.value;
        let phone = inputDOMSelectors.phoneInput.value;


        const httpHeaders = {
            method: "POST",
            body: JSON.stringify({ person, phone })
        };

        
        fetch(BASE_URL, httpHeaders)
        .then((res) => res.json())
        .then(() => {
            loadEventHandler();
            inputDOMSelectors.personInput.value = "";
            inputDOMSelectors.phoneInput.value = "";
        })
    


    }

    function deleteEventHandler(event) {
        const btnID = event.currentTarget.id;
        
        const httpHeaders = {
            method: "DELETE"
        }



        fetch(`${BASE_URL}${btnID}`, httpHeaders)
        .then((res) => res.json())
        .then(() => {
            loadEventHandler();
        })
    }

    async function loadEventHandler() {
        const dataAsResponse = await fetch(BASE_URL, {method: "GET"}); // getting the data as PROMISE format which later resolves to a "Response"
        let workingData = await dataAsResponse.json(); // Parsing the data into a JSON format {}
        workingData = Object.values(workingData); // Parsing the data from JSON format to an array that contains objects [ {"person": "Yavor", "phone": "+35978472328"}, {etc}, {etc} ]

        otherDOMSelectors.phoneBookContainer.innerHTML = "";

        for (const { person, phone, _id} of workingData) {  // Object destructing for loop


            const liElement = createElement('li', otherDOMSelectors.phoneBookContainer, `${person}: ${phone}`);
            const buttonEl = createElement('button', liElement, 'Delete');
            buttonEl.setAttribute("id", _id) // or could be done with => buttonEl.id = _id

            otherDOMSelectors.phoneBookContainer.appendChild(liElement);

            buttonEl.addEventListener('click', deleteEventHandler);

        }

        

        




    }



    function createElement(type, parentNode, content, classes, id, attributes, useInnerHtml) {
        const htmlElement = document.createElement(type);
    
        if (content && useInnerHtml) {
          htmlElement.innerHTML = content;
        } else {
          if (content && type !== "input") {
            htmlElement.textContent = content;
          }
    
        } if (content && type === "input") {
          htmlElement.value = content;
        }
    
        if (classes && classes.length > 0) {
          htmlElement.classList.add(...classes);
        }
    
        if (id) {
          htmlElement.id = id;
        }
    
        if (attributes) {
          for (const key in attributes) {
            htmlElement[key] = attributes[key];
          }
        }
    
        if (parentNode) {
          parentNode.appendChild(htmlElement);
        }
    
        return htmlElement
    
    
      }
}

attachEvents();
window.addEventListener('load', solve);

function solve() {

    const editSelectorsRef = {
        firstName: null,
        lastName: null,
        numberOfPeople: null,
        fromDate: null,
        numberOfDays: null
    }

    const inputDOMSelectors = {
        firstName: document.getElementById('first-name'),
        lastName: document.getElementById('last-name'),
        numberOfPeople: document.getElementById('people-count'),
        fromDate: document.getElementById('from-date'),
        numberOfDays: document.getElementById('days-count')
    };

    const otherDOMSelectors = {
        nextStepBtn: document.getElementById('next-btn'),
        ticketInfoContainer: document.querySelector(".ticket-info-container"),
        ticketInfoList: document.querySelector(".ticket-info-list"),
        confirmTicketContainer: document.querySelector(".confirm-ticket"),
        mainContainer: document.getElementById('main'),
        mainBody: document.getElementById('body')

    };

    otherDOMSelectors.nextStepBtn.addEventListener('click', nextStepHandler);


    function nextStepHandler(event) {
        event.preventDefault();

        let allFieldsAreValid = Object.values(inputDOMSelectors).every((input) => input.value !== "");

        if (!allFieldsAreValid) {
            return;
        }

        const {firstName, lastName, numberOfPeople, fromDate, numberOfDays} = inputDOMSelectors;
        const mainLiContainer = createElement("li", otherDOMSelectors.ticketInfoList, null, ['ticket']);
        const articleContainer = createElement('article', mainLiContainer);
        createElement('h3', articleContainer, `Name: ${firstName.value} ${lastName.value}`);
        createElement("p", articleContainer, `From date: ${fromDate.value}`);
        createElement('p', articleContainer, `For ${numberOfDays.value} days`);
        createElement("p", articleContainer, `For ${numberOfPeople.value} people`);

        const editBtn = createElement("button", mainLiContainer, "Edit", ['edit-btn']);
        const continueBtn = createElement("button", mainLiContainer, "Continue", ['continue-btn']);

        otherDOMSelectors.nextStepBtn.disabled = true;

        editBtn.addEventListener('click', editHandler);
        continueBtn.addEventListener('click', transferHandler);

        for (const key in inputDOMSelectors) {
            editSelectorsRef[key] = inputDOMSelectors[key].value;
        }

        clearAllInputs();



    }

    function confirmHandler() {
        otherDOMSelectors.mainContainer.remove();
        createElement('h1', otherDOMSelectors.mainBody, `Thank you, have a nice day!`, null, `thank-you`);
        const backBtn = createElement('button', otherDOMSelectors.mainBody, "Back", null, 'back-btn');

        backBtn.addEventListener('click', () => {
            window.location.reload();
        });


    }

    function transferHandler(event) {

        const dataRef = event.currentTarget.parentNode;

        const editBtn = dataRef.querySelector(".ticket > .edit-btn");
        const continueBtn = dataRef.querySelector('.ticket > .continue-btn');

        dataRef.classList = 'ticket-content';

        otherDOMSelectors.confirmTicketContainer.appendChild(dataRef);

        editBtn.remove();
        continueBtn.remove();

        const confirmBtn = createElement('button', dataRef, 'Confirm', ['confirm-btn']);
        const cancelBtn = createElement('button', dataRef, 'Cancel', ['cancel-btn']);

        confirmBtn.addEventListener('click', confirmHandler);
        cancelBtn.addEventListener('click', cancleTicketHandler);

    }

    function cancleTicketHandler(event) {
        event.currentTarget.parentNode.remove();
        otherDOMSelectors.nextStepBtn.removeAttribute('disabled');

    }

    function editHandler(event) {

        event.currentTarget.parentNode.remove();

        for (const key in inputDOMSelectors) {
            inputDOMSelectors[key].value = editSelectorsRef[key];
        }

        event.currentTarget.parentNode.innerHTML = "";
        otherDOMSelectors.nextStepBtn.removeAttribute('disabled');


    }

    function clearAllInputs() {
        Object.values(inputDOMSelectors).forEach((input) => {
            input.value = "";
        })
    }

    function createElement(type, parentNode, content, classes, id, attributes, useInnerHtml){
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

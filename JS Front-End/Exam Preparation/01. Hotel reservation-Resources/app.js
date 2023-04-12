window.addEventListener("load", solve);

function solve() {

    const inputDOMSelectors = {
        firstName: document.getElementById("first-name"),
        lastName: document.getElementById("last-name"),
        checkIn: document.getElementById("date-in"),
        checkOut: document.getElementById("date-out"),
        numberGuests: document.getElementById("people-count")
    };

    const otherDOMSelectors = {
        nextBtn: document.getElementById("next-btn"),
        liContainer: document.querySelector(".info-list"),
        confirmContainer: document.querySelector(".confirm-list"),
        verificationContainer: document.getElementById("verification")
    };

    const inputRefData = {
        firstName: null,
        lastName: null,
        checkIn: null,
        checkOut: null,
        numberGuests: null
    };

    otherDOMSelectors.nextBtn.addEventListener('click', nextEventHandler);

    function nextEventHandler(e) {
        e.preventDefault();
        

        const allInputsAreValid = Object.values(inputDOMSelectors).every((input) => input.value !== "");

        if (!allInputsAreValid) {
            return;
        }


        
        const {firstName, lastName, checkIn, checkOut, numberGuests} = inputDOMSelectors
        const liElement = createElement('li', otherDOMSelectors.liContainer, null, ['reservation-content']);
        const articleElement = createElement('article', liElement);
        createElement('h3', articleElement, `Name: ${firstName.value} ${lastName.value}`);
        createElement('p', articleElement, `From date: ${checkIn.value}`);
        createElement('p', articleElement, `To date: ${checkOut.value}`);
        createElement('p', articleElement, `For ${numberGuests.value} people`);

        const editBtn = createElement('button', liElement, 'Edit', ['edit-btn']);
        const continueBtn = createElement('button', liElement, 'Continue', ['continue-btn']);

        otherDOMSelectors.liContainer.appendChild(liElement);

        for (const key in inputDOMSelectors) {
            inputRefData[key] = inputDOMSelectors[key].value;
        }

        e.currentTarget.disabled = true; // disables the button
        clearAllInputs();

        editBtn.addEventListener('click', editEventHandler);
        continueBtn.addEventListener('click', () => {

            const dataRef = editBtn.parentNode;
            
            otherDOMSelectors.confirmContainer.appendChild(dataRef);

            editBtn.textContent = "Confirm";
            continueBtn.textContent = "Cancel";

            editBtn.classList = 'confirm-btn';
            continueBtn.classList = 'cancel-btn';

            editBtn.addEventListener(`click`, () => {  // Confirm Button

                editBtn.parentNode.remove();

                otherDOMSelectors.verificationContainer.classList.add('reservation-confirmed');
                otherDOMSelectors.verificationContainer.textContent = "Confirmed.";

                clearAllInputs();


            })

            continueBtn.addEventListener(`click`, () => {  // cancel button

                continueBtn.parentNode.remove();
                otherDOMSelectors.nextBtn.disabled = false;

                otherDOMSelectors.verificationContainer.classList.add('reservation-cancelled');
                otherDOMSelectors.verificationContainer.textContent = "Cancelled.";

                clearAllInputs();


            })

        });

    }


    function editEventHandler() {
        for (const key in inputDOMSelectors) {
            inputDOMSelectors[key].value = inputRefData[key];
        }

        otherDOMSelectors.liContainer.innerHTML = "";
        otherDOMSelectors.nextBtn.disabled = false;


    }

    function clearAllInputs() {
        Object.values(inputDOMSelectors).forEach((input) => {
            input.value = '';
        })
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

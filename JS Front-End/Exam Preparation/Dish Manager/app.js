window.addEventListener("load", solve);

function solve() {

  let counter = 0

  const inputDOM = {

    firstName: document.getElementById("first-name"),
    lastName: document.getElementById("last-name"),
    age: document.getElementById('age'),
    gender: document.getElementById("genderSelect"),
    dishDesc: document.getElementById("task")
  };

  const inputBackUp = {

    firstName: null,
    lastName: null,
    age: null,
    gender: null,
    dishDesc: null

  };

  const otherDOM = {

    submitBtn: document.getElementById('form-btn'),
    clearBtn: document.getElementById('clear-btn'),
    inProgress: document.getElementById("in-progress"),
    counterCon: document.getElementById("progress-count"),
    finishedCon: document.getElementById('finished')

  };

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

  otherDOM.submitBtn.addEventListener('click', submitEventHandler);
  otherDOM.clearBtn.addEventListener('click', clearEventHandler);


  function submitEventHandler() {

    const allInputsAreValid = Object.values(inputDOM).every((input) => input.value !== "");

    if (!allInputsAreValid) {
      return
    }
    

    const { firstName, lastName, age, gender, dishDesc } = inputDOM

    const liElement = createElement('li', otherDOM.inProgress, null, ['each-line']);
    const articleElement = createElement('article', liElement);
    createElement('h4', articleElement, `${firstName.value} ${lastName.value}`);
    createElement('p', articleElement, `${gender.value}, ${age.value}`);
    createElement('p', articleElement, `Dish description: ${dishDesc.value}`);

    const editBtn = createElement('button', liElement, `Edit`, [`edit-btn`]);
    const completeBtn = createElement('button', liElement, "Mark as complete", [`complete-btn`]);

    for (const key in inputDOM) {
      inputBackUp[key] = inputDOM[key].value;
    }

    clearAllInputs();

    counter ++;

    otherDOM.counterCon.innerHTML = '';
    otherDOM.counterCon.innerHTML = `${counter}`;


    editBtn.addEventListener('click', () => {

      

      editBtn.parentNode.remove();

      
      const liParent = editBtn.parentNode
      const articleParent = liParent.querySelector('article')
      let [firstName, lastName] = articleParent.querySelector('h4').textContent.split(' ');
      let [ageGender, descContainer] = articleElement.querySelectorAll('p');
      let [gender, age] = ageGender.textContent.split(", ")
      let [_, realDesc] = descContainer.textContent.split(": ")

      const editData = {
        
        firstName: firstName,
        lastName: lastName,
        age: age,
        gender: gender,
        dishDesc: realDesc
        
      }


      for (const key in inputDOM) {
        inputDOM[key].value = editData[key];
      }

      counter -= 1;

      otherDOM.counterCon.innerHTML = `${counter}`;
      

    })

    completeBtn.addEventListener('click', () => {

      const dataRef = completeBtn.parentNode

      otherDOM.finishedCon.appendChild(dataRef);

      counter -= 1;

      otherDOM.counterCon.innerHTML = `${counter}`;

      editBtn.remove();
      completeBtn.remove();


    })


    
    




  }

  function clearEventHandler(e) {

    otherDOM.finishedCon.innerHTML = "";

  }

  function clearAllInputs() {
    Object.values(inputDOM).forEach((input) => {
      input.value = "";
    })
  }



}

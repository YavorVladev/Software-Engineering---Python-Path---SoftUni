// TODO:
function attachEvents() {

    const BASE_URL = `http://localhost:3030/jsonstore/tasks/`;

    const inputDOM = {
        titleContainer: document.getElementById("title"),
        descContainer: document.getElementById("description")
    };

    const otherDOM = {
        loadBtn: document.getElementById("load-board-btn"),
        addTaskBtn: document.getElementById("create-task-btn"),
        toDoSection: document.querySelector("#todo-section .task-list"),
        inProgress: document.querySelector("#in-progress-section .task-list"),
        codeReview: document.querySelector("#code-review-section .task-list"),
        doneSection: document.querySelector("#done-section .task-list"),

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

      otherDOM.loadBtn.addEventListener('click', loadEventHandler);
      otherDOM.addTaskBtn.addEventListener('click', addTaskHandler);



      async function loadEventHandler() {


        [otherDOM.toDoSection, otherDOM.inProgress, otherDOM.codeReview, otherDOM.doneSection].forEach((input) => {
            input.innerHTML = "";
        })


        

        const dataRes = await fetch(BASE_URL);
        let workingData = await dataRes.json();
        workingData = Object.values(workingData);



        for (const { title, description, status, _id } of workingData) {

            if (status === "ToDo") {

                
                const liElement = createElement('li', otherDOM.toDoSection, null, ['task']);
                createElement('h3', liElement, title);
                createElement('p', liElement, description);
                const moveBtn = createElement('button', liElement, "Move to In Progress");


                otherDOM.toDoSection.appendChild(liElement)

                moveBtn.addEventListener('click', () => {

                    clearAllInputs();

                    const dataRef = moveBtn.parentNode


                    const taskID = _id;
                    const newStatus = "In Progress";


                    const httpHeaders = {
                        method: "PATCH",
                        headers: {"Content-Type": "application/json"},
                        body: JSON.stringify({ status: newStatus })

                    }

                    fetch(`${BASE_URL}${taskID}`, httpHeaders)
                        .then((res) => res.json())
                        .then(() => {
                            otherDOM.inProgress.appendChild(dataRef);
                            loadEventHandler();

                        })

                })

                

            } else if (status === "In Progress") {


                const liElement = createElement('li', otherDOM.inProgress, null, ['task']);
                createElement('h3', liElement, title);
                createElement('p', liElement, description);
                const moveBtn = createElement('button', liElement, "Move to Code Review");


                otherDOM.inProgress.appendChild(liElement)

                moveBtn.addEventListener('click', () => {

                    clearAllInputs();

                    const dataRef = moveBtn.parentNode


                    const taskID = _id;
                    const newStatus = "Code Review";

                    const httpHeaders = {
                        method: "PATCH",
                        headers: {"Content-Type": "application/json"},
                        body: JSON.stringify({ status: newStatus })

                    }

                    fetch(`${BASE_URL}${taskID}`, httpHeaders)
                        .then((res) => res.json())
                        .then(() => {
                            otherDOM.codeReview.appendChild(dataRef);
                            loadEventHandler();

                        })

                })

            } else if (status === "Code Review") {


                const liElement = createElement('li', otherDOM.codeReview, null, ['task']);
                createElement('h3', liElement, title);
                createElement('p', liElement, description);
                const moveBtn = createElement('button', liElement, "Move to Done");


                otherDOM.codeReview.appendChild(liElement)

                moveBtn.addEventListener('click', () => {

                    clearAllInputs();

                    const dataRef = moveBtn.parentNode


                    const taskID = _id;
                    const newStatus = "Done";

                    const httpHeaders = {
                        method: "PATCH",
                        headers: {"Content-Type": "application/json"},
                        body: JSON.stringify({ status: newStatus })

                    }

                    fetch(`${BASE_URL}${taskID}`, httpHeaders)
                        .then((res) => res.json())
                        .then(() => {
                            otherDOM.doneSection.appendChild(dataRef);
                            loadEventHandler();

                        })

                })

            } else {

                const liElement = createElement('li', otherDOM.doneSection, null, ['task']);
                createElement('h3', liElement, title);
                createElement('p', liElement, description);
                const moveBtn = createElement('button', liElement, "Close");


                otherDOM.doneSection.appendChild(liElement)

                moveBtn.addEventListener('click', () => {

                    

                    const dataRef = moveBtn.parentNode


                    const taskID = _id;

                    const httpHeaders = {
                        method: "DELETE",

                    }

                    fetch(`${BASE_URL}${taskID}`, httpHeaders)
                        .then((res) => res.json())
                        .then(() => {
                            dataRef.remove();
                            loadEventHandler();
                            clearAllInputs();

                        })

                })

            }


        

        }

      }

      function addTaskHandler() {

        

        const title = inputDOM.titleContainer.value;
        const description = inputDOM.descContainer.value;

        clearAllInputs();

        const newTask = {
            title: title,
            description: description,
            status: "ToDo"
        }
        

        const httpHeaders = {
            method: "POST",
            body: JSON.stringify(newTask)
        }

        fetch(BASE_URL, httpHeaders)
            .then((res) => res.json())
            .then(() => {
                clearAllInputs();
                loadEventHandler();
                
            })



      }

      function clearAllInputs() {
        Object.values(inputDOM).forEach((input) => {
            input.value = '';
        })
      }


      

}

attachEvents();
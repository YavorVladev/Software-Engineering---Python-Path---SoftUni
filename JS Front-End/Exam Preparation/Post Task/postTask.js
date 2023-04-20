function solve() {

    const inputDOMS = {
        title: document.getElementById('task-title'),
        category: document.getElementById('task-category'),
        content: document.getElementById('task-content'),
    };

    const storage = {
        title: null,
        category: null,
        content: null
    };

    const otherDOMS = {
        publishBtn: document.getElementById("publish-btn"),
        reviewList: document.getElementById("review-list"),
        publishedList: document.getElementById("published-list")
    };

    otherDOMS.publishBtn.addEventListener("click", publishEventHandler)

    function publishEventHandler() {

        const allFieldsAreValid = Object.values(inputDOMS).every((input) => input.value !== "");

        if (!allFieldsAreValid) {
            return;
        }

        const { title, category, content } = inputDOMS


        const liElement = createElement("li", otherDOMS.reviewList, null, ['rpost']);
        const articleElement = createElement('article', liElement);
        createElement('h4', articleElement, `${title.value}`);
        createElement('p', articleElement, `Category: ${category.value}`);
        createElement('p', articleElement, `Content: ${content.value}`);

        const editBtn = createElement('button', liElement, `Edit`, ['action-btn', `edit`]);
        const postBtn = createElement('button', liElement, `Post`, ['action-btn', `post`]);

        for (const key in inputDOMS) {
            storage[key] = inputDOMS[key].value;
        }

        otherDOMS.reviewList.appendChild(liElement);

        clearAllInputs();


        // edit btn 

        editBtn.addEventListener("click", () => {

            for (const key in inputDOMS) {
                inputDOMS[key].value = storage[key];
            }

            editBtn.parentNode.remove();

        })

        // post btn

        postBtn.addEventListener('click', () => {

            const dataRef = postBtn.parentNode

            console.log(dataRef)

            otherDOMS.publishedList.appendChild(dataRef);

            editBtn.remove();
            postBtn.remove();


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

    function clearAllInputs() {
        Object.values(inputDOMS).forEach((input) => {
            input.value = "";
        })
    }
  
}
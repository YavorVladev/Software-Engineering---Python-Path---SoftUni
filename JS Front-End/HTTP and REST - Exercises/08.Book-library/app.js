function attachEvents() {

  const BASE_URL = `http://localhost:3030/jsonstore/collections/books/`;

  const inputDOMSelectors = {
    titleContainer: document.querySelector('input[name="title"]'),
    auhtorContainer: document.querySelector('input[name="author"]')
  }

  const otherDOMSelectors = {
    loadAllBooksBtn: document.getElementById("loadBooks"),
    submitBtn: document.querySelector("#form > button"),
    booksContainer: document.querySelector("table > tbody"),
    formContainer: document.querySelector("#form > h3")

  }

  let editBookID = null;

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



  otherDOMSelectors.loadAllBooksBtn.addEventListener('click', loadEventHandler);
  otherDOMSelectors.submitBtn.addEventListener('click', submitEventHandler);

  async function loadEventHandler() {

    otherDOMSelectors.booksContainer.innerHTML = "";

    const booksRes = await fetch(BASE_URL);
    const booksData = await booksRes.json();

    for (const bookID in booksData) {
      const { author, title } = booksData[bookID];

      const tableRow = createElement('tr');
      const titleCol = createElement('td', tableRow, title);
      const authorCol = createElement('td', tableRow, author);
      const buttonCol = createElement('td', tableRow);
      const editBtn = createElement('button', buttonCol, 'Edit', null, bookID);
      const deleteBtn = createElement('button', buttonCol, 'Delete', null, bookID);

      otherDOMSelectors.booksContainer.appendChild(tableRow);

      editBtn.addEventListener('click', () => {
        editBookID = bookID;
        otherDOMSelectors.formContainer.textContent = "Edit FORM";
        inputDOMSelectors.auhtorContainer.value = author;
        inputDOMSelectors.titleContainer.value = title;
        otherDOMSelectors.submitBtn.textContent = "Save";


      })

      deleteBtn.addEventListener('click', deleteEventHandler);

    }


  }

  async function deleteEventHandler() {
    const httpHeader = {
      method: "DELETE"
    }

    await fetch(`${BASE_URL}${this.id}`, httpHeader)
    loadEventHandler();
  }

  async function submitEventHandler() {

    let author = inputDOMSelectors.auhtorContainer.value;
    let title = inputDOMSelectors.titleContainer.value;

    if (author === ""|| title === "") {
      return;
    }

    const httpHeader = {
      method: "POST",
      body: JSON.stringify({ author, title })
    }

    let url = BASE_URL

    if (otherDOMSelectors.formContainer.textContent === "Edit FORM") {
      httpHeader.method = "PUT"
      url = `${BASE_URL}${editBookID}`
    }

    const resData = await fetch(url, httpHeader);
    loadEventHandler();

    if (otherDOMSelectors.submitBtn.textContent === "Save") {
      otherDOMSelectors.formContainer.textContent = "FORM"
      otherDOMSelectors.submitBtn.textContent = "Submit";

    }

    inputDOMSelectors.auhtorContainer.value = "";
    inputDOMSelectors.titleContainer.value = "";

  }


}

attachEvents();
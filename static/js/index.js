function loadData() {
  const loadMessage = document.getElementById("loadMessage");
  const blobLink = document.getElementById("blobLink");
  // Make loadedBlob invisible, and make loadingBlob visible.
  blobLink.style.display = "none";
  loadMessage.style.display = "block";
  // POST /people
  fetch("/people", { method: "POST" })
    .then((response) => response.text())
    .then((response) => {
      // Set loadedBlob to the link from the response.
      // Make loadedBlob visible, and make loadingBlob invisible.
      blobLink.href = response;
      blobLink.textContent = response;
      loadMessage.style.display = "none";
      blobLink.style.display = "block";
    });
}


function clearData() {
  const clearMessage = document.getElementById("clearMessage");
  clearMessage.textContent = "Please wait...";
  clearMessage.style.display = "block";
  fetch("/people", { method: "DELETE" })
    .then(() => {
      clearMessage.textContent = "The data has been cleared.";
    });
}


function queryData(form) {
  const queryMessage = document.getElementById("queryMessage");
  const queryResults = document.getElementById("queryResults");
  queryMessage.style.display = "block";
  const firstName = form.firstName.value;
  const lastName = form.lastName.value;
  const peopleUrl = formatPeopleUrl(firstName, lastName);
  fetch(peopleUrl)
    .then((response) => response.json())
    .then((response) => {
      const newTable = createTable(response);
      const currentTables = queryResults.getElementsByTagName("table");
      queryMessage.style.display = "none";
      if (currentTables?.length > 0) {
        queryResults.replaceChild(newTable, currentTables[0]);
      } else {
        queryResults.appendChild(newTable);
      }
    });
  return false;
}

function formatPeopleUrl(firstName, lastName) {
  let peopleUrl = "/people";
  if (firstName && lastName) {
    peopleUrl += `?firstName=${firstName}&lastName=${lastName}`;
  } else if (firstName) {
    peopleUrl += `?firstName=${firstName}`;
  } else if (lastName) {
    peopleUrl += `?lastName=${lastName}`;
  }
  return peopleUrl;
}

function createTable(json) {
  const headers = getHeadersFromJson(json);
  const table = document.createElement("table");
  const thead = createThead(headers);
  table.appendChild(thead);
  const tbody = createTbody(headers, json);
  table.appendChild(tbody);
  return table;
}

function getHeadersFromJson(json) {
  const headers = new Set();
  for (const element of json) {
    for (const header of Object.keys(element)) {
      headers.add(header);
    }
  }
  return headers;
}

function createThead(headers) {
  const thead = document.createElement("thead");
  const trHead = document.createElement("tr");
  for (const header of headers) {
    const th = document.createElement("th");
    th.textContent = header;
    trHead.appendChild(th);
  }
  thead.appendChild(trHead);
  return thead;
}

function createTbody(headers, json) {
  const tbody = document.createElement("tbody");
  for (const element of json) {
    const tr = document.createElement("tr");
    // Add a cell for every header, even if this object doesn't have it.
    for (const header of headers) {
      const td = document.createElement("td");
      const value = element[header];
      if (value !== undefined) {
        td.textContent = value;
      }
      tr.appendChild(td);
    }
    tbody.appendChild(tr);
  }
  return tbody;
}

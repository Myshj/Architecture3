var xhr = new XMLHttpRequest();
function processDELETEuser()
{
  try {
    // Якщо запит завершений...
    if (xhr.readyState == 4) {
        // і виконаний без помилок...
        if (xhr.status == 200) {
            // виконується обробка отриманих даних.
            location.reload();
            //postMessage(DoTask(task))

        // і виникла помилка...
        } else {
            // виконується сповіщення про помилку.
            alert("Не удалось получить данные:\n" +
                xhr.statusText);
        }
    }
  }
  catch( e ) {
       alert('Помилка: ' + e.description);
  }
}

function processDELETEemail()
{
  try {
    // Якщо запит завершений...
    if (xhr.readyState == 4) {
        // і виконаний без помилок...
        if (xhr.status == 200) {
            // виконується обробка отриманих даних.
            location.reload();
            //postMessage(DoTask(task))

        // і виникла помилка...
        } else {
            // виконується сповіщення про помилку.
            alert("Не удалось получить данные:\n" +
                xhr.statusText);
        }
    }
  }
  catch( e ) {
       alert('Помилка: ' + e.description);
  }
}

function processADDemail()
{
  try {
    // Якщо запит завершений...
    if (xhr.readyState == 4) {
        // і виконаний без помилок...
        if (xhr.status == 200) {
            // виконується обробка отриманих даних.
            location.reload();
            //postMessage(DoTask(task))

        // і виникла помилка...
        } else {
            // виконується сповіщення про помилку.
            alert("Не удалось получить данные:\n" +
                xhr.statusText);
        }
    }
  }
  catch( e ) {
       alert('Помилка: ' + e.description);
  }
}

function processADDuser()
{
  try {
    // Якщо запит завершений...
    if (xhr.readyState == 4) {
        // і виконаний без помилок...
        if (xhr.status == 200) {
            // виконується обробка отриманих даних.
            location.reload();
            //postMessage(DoTask(task))

        // і виникла помилка...
        } else {
            // виконується сповіщення про помилку.
            alert("Не удалось получить данные:\n" +
                xhr.statusText);
        }
    }
  }
  catch( e ) {
       alert('Помилка: ' + e.description);
  }
}

function processSETname()
{
  try {
    // Якщо запит завершений...
    if (xhr.readyState == 4) {
        // і виконаний без помилок...
        if (xhr.status == 200) {
            // виконується обробка отриманих даних.
            location.reload();
            //postMessage(DoTask(task))

        // і виникла помилка...
        } else {
            // виконується сповіщення про помилку.
            alert("Не удалось получить данные:\n" +
                xhr.statusText);
        }
    }
  }
  catch( e ) {
       alert('Помилка: ' + e.description);
  }
}

function deleteUser(user_id){

    xhr.open('DELETE', "/users/" + user_id, true);
    xhr.send(null);
    xhr.onreadystatechange = processDELETEuser;
}

function deleteEmail(user_id, email){
    xhr.open('DELETE', "/users/" + user_id + "/" + email, true);
    xhr.send(null);
    xhr.onreadystatechange = processDELETEemail;
}

function addEmail(user_id, email){
    xhr.open('POST', "/users/" + user_id + "/" + email, true);
    xhr.send(null);
    xhr.onreadystatechange = processADDemail;
}

function setUserName(user_id, user_name){
    xhr.open('PUT', "/users/" + user_id + "/" + user_name, true);
    xhr.send(null);
    xhr.onreadystatechange = processSETname;
}

function addUser(user_name, email){
    xhr.open('POST', "/users/" + user_name + "/" + email, true);
    xhr.send(null);
    xhr.onreadystatechange = processADDuser;
}
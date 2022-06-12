// async function checkHealth() {
//   var myHeaders = new Headers();
//   myHeaders.append("Accept", "application/json");

//   var requestOptions = {
//     method: "GET",
//     headers: myHeaders,
//     redirect: "follow",
//   };
//   var re;
//   await fetch("http://127.0.0.1:5000/api/v1", requestOptions)
//     .then((response) => {
//       response.json();
//     })
//     .then(function (result) {
//       console.log(result);
//       re = result;
//     })
//     .catch((error) => console.log("error", error));

//   return re.is_server_on;
// }

function checkedOrNot(item) {
  if (item) {
    return 1;
  }
  return 0;
}

async function send() {
  var myHeaders = new Headers();
  myHeaders.append("Accept", "application/json");

  var formdata = new FormData();

  formdata.append(
    "is_delete_on",
    checkedOrNot(document.querySelector("#is_delete_on").checked)
  );
  formdata.append(
    "is_new_headers_on",
    checkedOrNot(document.querySelector("#is_new_headers_on").checked)
  );
  formdata.append(
    "switch_to_next_on",
    checkedOrNot(document.querySelector("#switch_to_next_on").checked)
  );
  formdata.append(
    "delete_columns",
    document.querySelector("#delete_columns").value
  );
  formdata.append("headers", document.querySelector("#headers").value);
  formdata.append(
    "searching_column",
    document.querySelector("#searching_column").value
  );
  formdata.append(
    "searching_value",
    document.querySelector("#searching_value").value
  );
  formdata.append(
    "replaceValue",
    document.querySelector("#replaceValue").value
  );
  formdata.append("upload", document.getElementById("upload").files[0]);

  var requestOptions = {
    method: "POST",
    headers: myHeaders,
    body: formdata,
  };

  var re;
  await fetch("http://127.0.0.1:5000/api/v1/file", requestOptions)
    .then((response) => {
      re = response;
      return response.json();
    })
    .then((result) => {
      let errors = result["errors"];
      let messages = result["messages"];
      if (errors.length > 0) {
        document.querySelector("#errors").classList.remove("hidden");
        window.scrollTo({ top: 0, behavior: "smooth" });

        let body = document.querySelector("#errorsBody ul");
        body.innerHTML = "";
        errors.forEach((item) => {
          let li = document.createElement("li");
          li.appendChild(document.createTextNode(item));
          body.appendChild(li);
        });
      }
      if (messages.length > 0) {
        document.querySelector("#messages").classList.remove("hidden");
        window.scrollTo({ top: 0, behavior: "smooth" });

        let body = document.querySelector("#messagesBody ul");
        body.innerHTML = "";
        messages.forEach((item) => {
          let li = document.createElement("li");
          li.appendChild(document.createTextNode(item));
          body.appendChild(li);
        });
      }
      if (re.status == 200) {
        download();
      }
    })
    .catch((error) => {
      console.log("error", error);
      alert("error", error);
    });
}

async function download() {
  // window.location.href = "http://127.0.0.1:5000/api/v1/download";
  document.querySelector("#downloadLink").click();
}

// if (checkHealth()) {
//   send();
// download();
// } else {
// console.log("error");
// }

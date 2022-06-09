async function load() {
  var myHeaders = new Headers();
  myHeaders.append("Accept", "application/json");

  var requestOptions = {
    method: "GET",
    headers: myHeaders,
    redirect: "follow",
  };
  var re;
  await fetch("http://127.0.0.1:5000/api/v1", requestOptions)
    .then((response) => response.json())
    .then(function (result) {
      console.log(result);
      re = result;
    })
    .catch((error) => console.log("error", error));

  return re.is_server_on;
}

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
    checkedOrNot(document.querySelector("#is_delete_on").checked)
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
  console.log("Send");
  //FIXME: Can not get Response
  await fetch("http://127.0.0.1:5000/api/v1/file", requestOptions)
    .then((response) => response.json())
    .then((result) => console.log(result))
    .catch((error) => console.log("error", error));
}

async function download() {
  //FIXME: Can not Download The file
  var myHeaders = new Headers();
  myHeaders.append("Accept", "application/json");
  var requestOptions = {
    method: "GET",
    headers: myHeaders,
    redirect: "follow",
  };
  await fetch("http://127.0.0.1:5000/api/v1/download", requestOptions)
    .then((response) => {
      const reader = response.body.getReader();
      return new ReadableStream({
        start(controller) {
          return pump();
          function pump() {
            return reader.read().then(({ done, value }) => {
              // When no more data needs to be consumed, close the stream
              if (done) {
                controller.close();
                return;
              }
              // Enqueue the next data chunk into our target stream
              controller.enqueue(value);
              return pump();
            });
          }
        },
      });
    })
    .then((stream) => new Response(stream))
    .then((response) => response.blob())
    .then((blob) => URL.createObjectURL(blob))
    .catch((err) => console.error(err));
  console.log("downloaded");
}

if (load()) {
  //   send();
  // download();
} else {
  console.log("error");
}

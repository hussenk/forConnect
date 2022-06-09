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
      console.log("set value");
    })
    .catch((error) => console.log("error", error));

  return re.is_server_on;
}

async function send() {
  var myHeaders = new Headers();
  myHeaders.append("Accept", "application/json");

  var formdata = new FormData();
  formdata.append("is_delete_on", "1");
  formdata.append("is_new_headers_on", "1");
  formdata.append("switch_to_next_on", "0");
  formdata.append("delete_columns", "namxe,idx");
  formdata.append("headers", "ix,namx,isx,xx,x");
  formdata.append("searching_column", "namx");
  formdata.append("searching_value", "1234");
  formdata.append("replaceValue", "123");
  formdata.append("upload", fileInput.files[0], "Data.xlsx");

  var requestOptions = {
    method: "POST",
    headers: myHeaders,
    body: formdata,
    redirect: "follow",
  };

  await fetch("http://127.0.0.1:5000/api/v1/file", requestOptions)
    .then((response) => response.json())
    .then((result) => console.log(result))
    .catch((error) => console.log("error", error));
}

async function download() {
  var myHeaders = new Headers();
  myHeaders.append("Accept", "application/json");

  var requestOptions = {
    method: "GET",
    headers: myHeaders,
    redirect: "follow",
  };

  console.log('hi');
  await fetch("http://127.0.0.1:5000/api/v1/download", requestOptions)
    .then((response) => response.text())
    .then((result) => console.log(result))
    .catch((error) => console.log("error", error));
}
// console.log(load());
if (load()) {
  // send();
  download();
} else {
  console.log("error");
}

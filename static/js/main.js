function load() {
  var xhttp = new XMLHttpRequest();
  console.log("xhttp");
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      console.log("true");
      //   document.getElementById("demo").innerHTML = this.responseText;
    }
  };

  xhttp.open("GET", "http://127.0.0.1:5000/api/v1");
    xhttp.send();
  console.log(xhttp);
  console.log(xhttp);
}

load();

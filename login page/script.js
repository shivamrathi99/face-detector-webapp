const name = document.getElementById("name");
const password = document.getElementById("password");
const form = document.getElementById("form");
const errorElement = document.getElementById("error");

form.addEventListener("submit", (e) => {
  let messages = [];
  if (password.value.length === "" || password.value != "a1b2c3") {
    alert("Please enter the correct password");
  }

  if (messages.length > 0) {
    e.preventDefault();
    errorElement.innerHTML = messages.join(" , ");
  }
});

function myfunction() {
  if (password.type === "password") {
    password.type = "text";
  } else {
    password.type = "password";
  }
}

//name == any random
//password == a1b2c3

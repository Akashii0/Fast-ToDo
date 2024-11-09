const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");
console.log(loginForm);
signupBtn.onclick = (()=>{
  loginForm.style.marginLeft = "-50%";
  loginText.style.marginLeft = "-50%";
});
loginBtn.onclick = (async ()=>{
  console.log("Loaded");
  loginForm.style.marginLeft = "0%";
  loginText.style.marginLeft = "0%";
  await loginUser();
});
signupLink.onclick = (()=>{
  signupBtn.click();
  return false;
});


async function loginUser() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  res = await fetch(
    "http://127.0.0.1:8000/login",
    data={
      "username": username,
      "password": password
    }
  )

  console.log(res);
  
}
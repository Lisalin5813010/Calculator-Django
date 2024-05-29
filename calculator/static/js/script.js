// script.js

function showMessage() {
  alert("Your diary has been saved!");
}

document.addEventListener('DOMContentLoaded', function() {
  var button = document.getElementById("myButton");
  if (button) {
      button.addEventListener('click', showMessage);
  }
});


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

function validateForm() {
  // Get the input fields and error message element
  var name = document.getElementById("name").value;
  var email = document.getElementById("age").value;
  var email = document.getElementById("gender").value;
  var errorMessage = document.getElementById("errorMessage");
  // Check if the fields are empty
  if (student_name === "" || student_age === "" || student_gender === "") {
      // Display the error message
      errorMessage.style.display = "block";
  } else {
      // Hide the error message
      errorMessage.style.display = "none";
      
      // Submit the form or perform desired action
      alert("Form submitted successfully!");
      // document.getElementById("myForm").submit(); // Uncomment to submit the form
  }
}

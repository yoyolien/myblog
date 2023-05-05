// Get the button element by its ID
const button = document.getElementById('my-button');

// Add a click event listener to the button
button.addEventListener('click', function() {
  // When the button is clicked, toggle the class of the navbar element
  const navbar = document.getElementById('my-navbar');
  navbar.classList.toggle('active');
});

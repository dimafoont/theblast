// STICKY HEADER

// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the header
var header = document.getElementById("myHeader");
const container = document.querySelector('.site-container');

// Get the offset position of the navbar
var sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset > sticky && window.innerWidth > 767) {
    header.classList.add("sticky");
    container.style.marginTop = '85px';
  } else {
    header.classList.remove("sticky");
    container.style.marginTop = '0px';
  }
}

// END STICKY HEADER

// MENU

var menuOpen = document.querySelector('.menu-open');
var menuClose = document.querySelector('.menu-close');
const menu = document.querySelector('.menu');

menuOpen.addEventListener('click', () => {
  menu.classList.add('menu-active');
  menuOpen.style.display = 'none';
  menuClose.style.display = 'block';
})

menuClose.addEventListener('click', () => {
  menu.classList.remove('menu-active');
  menuOpen.style.display = 'block';
  menuClose.style.display = 'none';
})


// END MENU
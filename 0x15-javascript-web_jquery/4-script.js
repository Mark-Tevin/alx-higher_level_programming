const $ = window.$;
// Attach a click event listener to the <div> with ID "toggle_header"
$('#toggle_header').bind('click', function () {
  $('header').toggleClass('green red');
});

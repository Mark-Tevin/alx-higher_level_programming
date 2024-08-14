//  updates the text of the <header> element to New Header!!!
$(document).ready(function () {
  $('#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});

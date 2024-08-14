// script that adds a <li> element to a list when the user clicks
// DIV#add_item tag
const $ = window.$;
$('#add_item').bind('click', function () {
  $('UL.my_list').append('<li>Item</li>');
});

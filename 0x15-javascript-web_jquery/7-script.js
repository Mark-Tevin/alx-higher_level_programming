// Script that fetches the character name from this URL
// https://swapi-api.hbtn.io/api/people/5/?format=json
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    $('#character').text(data.name);
  });
});

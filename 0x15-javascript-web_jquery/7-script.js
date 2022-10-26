const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, err) {
  $('DIV#character').text(data.name);
});

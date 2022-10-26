const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, err) {
  const anarray = data.results;
  for (let i = 0; i < anarray.length; i++) {
    $('UL#list_movies').append('<li>' + anarray[i].title + '</li>');
  }
});

//  script that fetches and lists the title for  movies by using this URL:
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    console.log(data);
    data.results.forEach(film => {
	$('UL#list_movies').append(film.title);
    });
});

#!/usr/bin/env node

async function loadList() {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
    if (!response.ok) {
      throw new Error('Request failed: ' + response.status);
    }
  const data = await response.json();
	const list_movies = document.querySelector('#list_movies');

	data.results.forEach(function (film) {
		const li = document.createElement('li');
		li.textContent = film.title;
		list_movies.append(li);
	});
  } catch (error) {
    console.error('Something went wrong:', error);
  }
}

loadList();



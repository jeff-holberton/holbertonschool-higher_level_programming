#!/usr/bin/env node

const header = document.querySelector('header');
const toggle_header = document.querySelector('#toggle_header');

toggle_header.addEventListener('click', function() {
	header.classList.toggle('red');
	header.classList.toggle('green')
});

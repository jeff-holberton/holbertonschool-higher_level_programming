#!/usr/bin/env node

async function loadHello() {
  try {
    const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
    if (!response.ok) {
      throw new Error('Request failed: ' + response.status);
    }
	const data = await response.json();

	const hello = document.querySelector('#hello');
	hello.textContent = data.hello;
  } catch (error) {
    console.error('Something went wrong:', error);
  }
}

loadHello();



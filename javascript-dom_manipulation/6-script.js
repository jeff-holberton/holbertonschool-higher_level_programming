#!/usr/bin/env node

async function loadCharacter() {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
    if (!response.ok) {
      throw new Error('Request failed: ' + response.status);
    }
    const data = await response.json();
    document.querySelector('#character').textContent = data.name
  } catch (error) {
    console.error('Something went wrong:', error);
  }
}

loadCharacter();



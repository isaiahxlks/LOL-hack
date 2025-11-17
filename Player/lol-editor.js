// Legends of Learning Level Editor
// Usage: node lol-level.js

function setCookie(name, value, days) {
  const expires = new Date();
  expires.setTime(expires.getTime() + days * 24 * 60 * 60 * 1000);
  document.cookie = `${name}=${value}; expires=${expires.toUTCString()}; path=/`;
}

async function editLevel(newLevel) {
  // Fetch player_data from the current page
  const response = await fetch('https://www.legendsoflearning.com/');
  const playerData = (await response.text()).match(/player_data=([^;]+)/);

  if (!playerData) {
    console.error('Failed to extract player_data from the page.');
    return;
  }

  // Extract the existing level from player_data
  const playerDataString = playerData[1];
  const existingLevel = JSON.parse(atob(playerDataString)).level;

  console.log(`Current level: ${existingLevel}`);

  // Set the new level and update the cookie
  const updatedPlayerData = btoa(JSON.stringify({
    ...JSON.parse(atob(playerDataString)),
    level: newLevel,
  }));

  setCookie('player_data', updatedPlayerData, 365);
  console.log(`Level set to ${newLevel}`);
}

// Example usage: Set level to 10
editLevel(10);

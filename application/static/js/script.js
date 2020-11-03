// application/static/js/script.js

"use strict";


// Dark/Light theme toggle.

let darktheme = localStorage.getItem('darktheme');

const themeToggleButton = document.querySelector('.toggle-theme');

const enableDarkTheme = () => {
    document.body.classList.add('dark-theme');
    localStorage.setItem('darktheme', 'enabled');
    themeToggleButton.textContent = 'light theme';
}

const disableDarkTheme = () => {
    document.body.classList.remove('dark-theme');
    localStorage.setItem('darktheme', 'disabled');
    themeToggleButton.textContent = 'dark theme';
}

if (darktheme === 'enabled') {
    enableDarkTheme();
}

if (themeToggleButton) {
    themeToggleButton.addEventListener('click', () => {
        darktheme = localStorage.getItem('darktheme');
        if (darktheme === 'disabled') {
            enableDarkTheme();
        } else {
            disableDarkTheme();
        }
    });
}

// Close flash messages.

const closeMessageButton = document.querySelector('.close');

closeMessageButton.addEventListener('click', () => {
    document.querySelector('.message').remove();
});

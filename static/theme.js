/* function quickTest() {
    alert("OH HELLO THERE");
}

let darkMode = localStorage.getItem('darkMode');
const darkModeToggle = document.querySelector('#dark-mode-toggle');
const darkModeToggleTable = document.querySelector('#col-md-12');

// Check if dark mode is enabled 
// if enabled turn it off
// if disabled, turn it on

const enableDarkMode = () => {
    // 1. Add class darkmode to body
    document.body.classList.add('darkmode');
    // 2. Update darkMode in the localstorage
    localStorage.setItem('darkMode', 'enabled');
};

const disableDarkMode = () => {
    document.body.classList.remove('darkmode');

    localStorage.setItem('darkMode', null);
};

if (darkMode === 'enabled') {
    enableDarkMode();
}

darkModeToggle.addEventListener('click', () => {
    // Quick update to the actual variable.
    darkMode = localStorage.getItem('darkMode');
    if (darkMode !== 'enabled') {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
});
*/
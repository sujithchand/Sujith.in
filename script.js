// Dark Mode Toggle
const themeToggle = document.getElementById('theme-toggle');
themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    themeToggle.textContent = document.body.classList.contains('dark-theme') ? 'Light Mode' : 'Dark Mode';
});

// Greeting Based on Time of Day
function displayGreeting() {
    const hours = new Date().getHours();
    let greeting = "Hello!";
    if (hours >= 5 && hours < 12) greeting = "Good Morning!";
    else if (hours >= 12 && hours < 18) greeting = "Good Afternoon!";
    else greeting = "Good Evening!";
    
    document.getElementById('greeting').textContent = `${greeting} I'm John Doe`;
}
displayGreeting();

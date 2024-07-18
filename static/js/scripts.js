document.addEventListener('DOMContentLoaded', (event) => {
    let timer = 60;
    const timerElement = document.getElementById('timer');
    if (!timerElement) {
        const newTimerElement = document.createElement('div');
        newTimerElement.id = 'timer';
        newTimerElement.style.fontSize = '20px';
        newTimerElement.style.marginTop = '20px';
        document.body.appendChild(newTimerElement);
    }

    function startTimer() {
        const countdown = setInterval(() => {
            timer--;
            timerElement.textContent = `Time left: ${timer} seconds`;

            if (timer <= 0) {
                clearInterval(countdown);
                document.querySelector('form').submit(); // Auto-submit form after 1 minute
            }
        }, 1000);
    }

    startTimer();

    const feedbackElement = document.getElementById('feedback');
    if (feedbackElement) {
        feedbackElement.classList.add('visible');
        setTimeout(() => {
            feedbackElement.classList.remove('visible');
        }, 3000); // Hide feedback after 3 seconds
    }
});

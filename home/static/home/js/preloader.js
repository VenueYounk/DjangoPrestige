// script.js
window.addEventListener('load', function() {
    const preloader = document.querySelector('.preloader');
    const minimumPreloaderDuration = 0; // Время в миллисекундах (1 секунда)
    // Показываем прелоадер

    // Устанавливаем таймер для скрытия прелоадера после заданной продолжительности
    setTimeout(function() {
        preloader.classList.add('hidden');
        document.documentElement.style.overflow = 'visible';


    }, minimumPreloaderDuration);
});

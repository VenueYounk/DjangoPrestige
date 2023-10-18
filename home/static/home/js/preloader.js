var logoProgress
// script.js
const r = new rive.Rive({
    src: "/static/home/images/preloader/prestige.riv",
    canvas: document.getElementById("preloader_canvas"),
    autoplay: true,
    stateMachines: "State Machine 1",
    onLoad: () => {
        statesInput = r.stateMachineInputs('State Machine 1')
        logoProgress = statesInput[0]

        r.resizeDrawingSurfaceToCanvas();
        sayMeTheTruth()
    },
  });



function sayMeTheTruth(){ 
    logoProgress.value = 0
}





window.addEventListener('load', function() {
    const preloader = document.querySelector('.preloader');
    const minimumPreloaderDuration = 1000; // Время в миллисекундах (1 секунда)
    // Показываем прелоадер
    setProgressBar()
    // Устанавливаем таймер для скрытия прелоадера после заданной продолжительности
    setTimeout(function() {
        preloader.classList.add('hidden');
        document.documentElement.style.overflowY = 'overlay';


    }, minimumPreloaderDuration);


});

function increaseProgressBar() {
    logoProgress.value++
}


function easeInOutCubic(t) {
    if (t < 0.5) {
        return 4 * t * t * t;
    } else {
        const factor = ((2 * t) - 2);
        return 0.5 * factor * factor * factor + 1;
    }
}

function setProgressBar() {
    for (let index = 0; index <= 100; index++) {
        const interval = easeInOutCubic(index / 100) * 1000; 
        setTimeout(increaseProgressBar, interval);
        
        
    }
}

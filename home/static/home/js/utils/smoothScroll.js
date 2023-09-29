// Функция для плавной прокрутки к элементу
function smoothScroll(target) {
    const element = document.querySelector(target);
    console.log(element)
    if (element) {
        window.scrollTo({
            top: element.offsetTop,
            behavior: 'smooth'
        });
    }
}

// Обработчик события для ссылок в навигации
const navLinks = document.querySelectorAll('.smooth-scroll');
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault(); // Предотвращаем стандартное поведение ссылки
        const targetId = link.getAttribute('href'); // Получаем цель ссылки (например, "#section1")
        smoothScroll(targetId); // Вызываем функцию плавной прокрутки
    });
});




// Получаем все элементы с классом "card_employee-accordion"
var accordions = document.querySelectorAll(".card_employee-accordion");

// Добавляем обработчик события для каждого элемента
accordions.forEach(function (accordion) {
    accordion.addEventListener("click", function () {
        // Получаем соседний элемент с классом "card_employee-text"
        var parent = this.parentElement;

        // Получаем соседний элемент .card_employee-text внутри родителя
        var textElement = parent.querySelector(".card_employee-text")
        var pointer = accordion.querySelector(".accordion-pointer")
        // Добавляем или удаляем класс "toggled" у соседнего элемента
        textElement.classList.toggle("card_employed-text-visible");
        pointer.classList.toggle('accordion_openned')
    });
});
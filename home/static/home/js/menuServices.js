// Получаем ссылки на элементы
const categoryItems = document.querySelectorAll('.header_category');
const serviceLists = document.querySelectorAll('.services_from_category');

// Добавляем обработчик событий для элементов категорий
categoryItems.forEach(item => {
  item.addEventListener('click', () => {
    // Удаляем класс 'active' у всех списков услуг
    serviceLists.forEach(list => {
      list.classList.remove('active');
    });

    // Получаем выбранную категорию из атрибута 'data-category'
    const selectedCategory = item.getAttribute('data-category');

    // Находим соответствующий список услуг и добавляем ему класс 'active'
    const selectedServiceList = document.querySelector(`[data-services="${selectedCategory}"]`);
    selectedServiceList.classList.add('active');
  });
});

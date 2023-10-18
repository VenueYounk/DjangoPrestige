// Замените 'YOUR_BOT_TOKEN' на токен вашего Telegram-бота
const botToken = '6064740060:AAF7odbbEV7pyyTOOQ0RJmufv242FtJ4-gM';
// Замените 'YOUR_CHAT_ID' на ID чата, куда вы хотите отправить сообщение
const chatId = '767736461';

document.getElementById('my_form').addEventListener('submit', function (e) {
    e.preventDefault();

    // Собираем данные из формы
    const phoneNumber = document.querySelector('input[name="phone_number"]').value;
    const name = document.querySelector('input[name="name"]').value;
    const consent = document.querySelector('input[name="consent"]').checked ? 'Да' : 'Нет';

    // Формируем текст сообщения
    const messageText = `Новая заявка:\n\nИмя: ${name}\nНомер: ${phoneNumber}\nСогласие на обработку данных: ${consent}`;

    // Отправляем запрос к Telegram Bot API
    fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            chat_id: chatId,
            text: messageText
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.ok) {
            alert('Сообщение успешно отправлено в Telegram бота!');
        } else {
            alert('Произошла ошибка при отправке сообщения в Telegram бота.');
        }
    })
    .catch(error => {
        console.error('Произошла ошибка при отправке запроса:', error);
    });
});
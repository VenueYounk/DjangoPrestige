const showPopUpButton = document.querySelectorAll('.popup_start')
const popup = document.querySelector("#feedback_start")
const blur_div = document.querySelector(".blur")
const start_conversation = document.getElementById("start_conversation")
const end_conversation = document.getElementById("end_conversation")
const sendButtons = document.querySelectorAll('.send_info')

const botToken = '6064740060:AAF7odbbEV7pyyTOOQ0RJmufv242FtJ4-gM';
const chatId = '-969628829';

function  send(e) {
    e.preventDefault();

    // Собираем данные из формы
    const phoneNumbers = [];
    const names = [];
    const consent = document.querySelector('input[name="consent"]').checked ? 'Да' : 'Нет';

    // Собираем значения из всех полей с именем "phone_number" и "name"
    const phoneNumberInputs = document.querySelectorAll('input[name="phone_number"]');
    phoneNumberInputs.forEach(input => {
        const phoneNumber = input.value.trim(); // Удаляем лишние пробелы
        if (phoneNumber !== '') {
            phoneNumbers.push(phoneNumber);
        }
    });

    const nameInputs = document.querySelectorAll('input[name="name"]');
    nameInputs.forEach(input => {
        const nameValue = input.value.trim(); // Удаляем лишние пробелы
        if (nameValue !== '') {
            names.push(nameValue);
        }
    });

    console.log(names, consent, phoneNumbers);

    let messageText = `Новая заявка:\n\n`;

    if (names.length > 0) {
        messageText += `Имя: ${names.join(', ')}\n`;
    }

    if (phoneNumbers.length > 0) {
        messageText += `Номер(а): ${phoneNumbers.join(', ')}\n`;
    }


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
        start_conversation.style.display = "none";
        end_conversation.style.display = 'unset'
    })
    .catch(error => {
        console.error('Произошла ошибка при отправке запроса:', error);
    });
};


document.getElementById('my_form').addEventListener('submit', send)

showPopUpButton.forEach(function(buttons) {
    buttons.addEventListener("click", function() {
      console.log('togled')
      popup.classList.toggle("visible");
      blur_div.classList.toggle("blur_active")
    });
  });

blur_div.addEventListener("click", function() {
    popup.classList.remove("visible");
    blur_div.classList.remove("blur_active")
})


sendButtons.forEach(function(buttons) {
    buttons.addEventListener("click", send)
})




function submitOrder(event) {

    event.preventDefault();

    const name = document.getElementById('name').value;
    const address = document.getElementById('address').value;
    const phone = document.getElementById('phone').value;
    const requests = document.getElementById('requests').value;
    const datetime = document.getElementById('datetime').value;
    const payment = PAYMETHOD()

    //  Проверка на дату и время
    let currentDate = new Date();

    // Добавляем 40 минут к текущей дате
    currentDate.setMinutes(currentDate.getMinutes() + 59);

    let dateTime = new Date(datetime);

    // Получаем текущий час для проверки времени в интервале
    let datetimeHour = dateTime.getHours();

    let message = document.querySelector('.message-for-not-information')
    let message2 = document.querySelector('.message-for-not-basket')
    let message3 = document.querySelector('.message-for-not-time')
    let message4 = document.querySelector('.message-for-not-time-cor')

    if (name === '' || address === '' || phone === '' || payment === null || datetime === '') {
        message.classList.add('active-message')
        message.classList.add('b')
        setTimeout(() => {
        message.classList.remove('active-message')
        message.classList.add('c')
        message.classList.remove('b')
        setTimeout(() => {message.classList.remove('c')}, 1000)
    }, 2000);
    } else if (basket.length === 0) {
        message2.classList.add('active-message')
        message2.classList.add('b')
        setTimeout(() => {
        message2.classList.remove('active-message')
        message2.classList.add('c')
        message2.classList.remove('b')
        setTimeout(() => {message2.classList.remove('c')}, 1000)
    }, 2000);
    } else if (dateTime < currentDate) {
        message3.classList.add('active-message')
        message3.classList.add('b')
        setTimeout(() => {
        message3.classList.remove('active-message')
        message3.classList.add('c')
        message3.classList.remove('b')
        setTimeout(() => {message3.classList.remove('c')}, 1000)
    }, 2000);
    } else if ((datetimeHour >= 23 && datetimeHour <= 23 && dateTime.getMinutes() >= 59) || (datetimeHour >= 0 && datetimeHour <= 6)) {
        message4.classList.add('active-message')
        message4.classList.add('b')
        setTimeout(() => {
        message4.classList.remove('active-message')
        message4.classList.add('c')
        message4.classList.remove('b')
        setTimeout(() => {message4.classList.remove('c')}, 1000)
    }, 2000);
    } else {

        const formData = {
            operation: 1,
            name: name,
            address: address,
            phone: phone,
            requests: requests,
            payment: payment,
            basket: basket,
            datetime: datetime
        };


        fetch('http://localhost:5000/backend-endpoint', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
            .then(response => response.json())
            .then(data => {
                console.log('Успешно:', data);
            })
            .catch(error => {
                console.log('Ошибка:', error);
            });

        submitOrder2()
    }
}

function submitOrder2() {
    const name = document.getElementById('name').value;
    const address = document.getElementById('address').value;
    const phone = document.getElementById('phone').value;
    const requests = document.getElementById('requests').value;
    const datetime = document.getElementById('datetime').value;
    const payment = PAYMETHOD()

    const formData = {
        operation: 3,
        name: name,
        address: address,
        phone: phone,
        requests: requests,
        payment: payment,
        basket: basket,
        datetime: datetime
    };


    fetch('http://localhost:5000/backend-endpoint', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        window.location.href = "file:///D:/foodgo/thankpage.html";
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}
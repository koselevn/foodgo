function submitOrder(event) {

    event.preventDefault();

    const name = document.getElementById('name').value;
    const address = document.getElementById('address').value;
    const phone = document.getElementById('phone').value;
    const requests = document.getElementById('requests').value;
    const datetime = document.getElementById('datetime').value;
    const payment = PAYMETHOD()

    let message = document.querySelector('.message-for-not-information')
    let message2 = document.querySelector('.message-for-not-basket')

    if (name === '' || address === '' || phone === '' || payment === null) {
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
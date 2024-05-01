function accept(id) {
    let cart = document.querySelector('.cart')
    let btnDiv = document.querySelector(`[key_acept="${id}"]`);

    statuscooking(id)

    btnDiv.innerHTML = `<button class="cart-accept-btn" onclick="drivery(${id})">Drivery</button>`
}

function drivery(id) {
    let cart = document.querySelector('.cart')
    let btnDiv = document.querySelector(`[key_acept="${id}"]`)

    btnDiv.innerHTML = `    
    <input type="text" key_input="${id}" class="input-driv">
    <button onclick="delOrder(${id})" class="sent">Sent</button>`
}

function delOrder(id) {
    let cart = document.querySelector(`[key_acept_cart="${id}"]`)
    let input = document.querySelector(`[key_input="${id}"]`).value

    let message = document.querySelector('.invalid-2')
    let message2 = document.querySelector('.valid-3')

    const formData = {
        operation: 1,
        id: id,
        id_cr: input
    };


    fetch('http://localhost:5000/backend-endpoint9', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        console.log(data.couriers)
        data.couriers.map(el => {
            if (el.courier_id === parseInt(input)) {
                // message2.classList.add('active-message')
                // message2.classList.add('b')
                // setTimeout(() => {
                //     message2.classList.remove('active-message')
                //     message2.classList.add('c')
                //     message2.classList.remove('b')
                //     setTimeout(() => {message2.classList.remove('c')}, 1000)
                // }, 2000);
                statuscookingWay(id)
                cart.remove()
            } else {  
                // message.classList.add('active-message')
                // message.classList.add('b')
                // setTimeout(() => {
                //     message.classList.remove('active-message')
                //     message.classList.add('c')
                //     message.classList.remove('b')
                //     setTimeout(() => {message.classList.remove('c')}, 1000)
                // }, 2000);
            }
        })
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}

// --------------------------------statuscooking---------

function statuscooking(id) {

    const formData = {
        operation: 1,
        id: id,
    };


    fetch('http://localhost:5000/backend-endpoint7', {
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
}

// --------------------------------status---------

function statuscookingWay(id) {

    const formData = {
        operation: 1,
        id: id,
    };


    fetch('http://localhost:5000/backend-endpoint8', {
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
}
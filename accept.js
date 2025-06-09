function accept(id) {
    let cart = document.querySelector('.cart')
    let btnDiv = document.querySelector(`[key_acept="${id}"]`);

    statuscooking(id)

    btnDiv.innerHTML = `<button class="cart-accept-btn" onclick="drivery(${id})">Drivery</button>`
}

function drivery(id) {
    let btnDiv = document.querySelector(`[key_acept="${id}"]`);

    fetch('http://localhost:5000/get-couriers')
        .then(response => response.json())
        .then(data => {
            const couriers = data.couriers;

            let selectHTML = `<select class="input-driv" key_select="${id}">`;
            couriers.forEach(courier => {
                selectHTML += `<option value="${courier.courier_id}">${courier.courer_name} (ID: ${courier.courier_id})</option>`;
            });
            selectHTML += `</select>`;

            btnDiv.innerHTML = `
                ${selectHTML}
                <button onclick="delOrder(${id})" class="sent">Send</button>
            `;
        })
        .catch(error => {
            console.log("Ошибка при получении курьеров:", error);
        });
}

function delOrder(id) {
    let cart = document.querySelector(`[key_acept_cart="${id}"]`)
    let select = document.querySelector(`[key_select="${id}"]`)
    let input = select ? select.value : null;

    if (!input) {
        alert("Оберіть кур'єра");
        return;
    }

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
        statuscookingWay(id)
        cart.remove();
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
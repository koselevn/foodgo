let elemId = []
let elinSEL = []

function adminLog(event) {

    event.preventDefault();

    let login = document.querySelector('.login').value;
    let password = document.querySelector('.password').value;
    let message = document.querySelector('.invalid')
    let messageOk = document.querySelector('.ok_log_in');
    let form = document.querySelector('.form-log')
    let inf = document.querySelector('.order-section')
    let header = document.querySelector('.header-header')

    const formData = {
        operation: 4,
        login: login,
        password: password
    };


    fetch('http://localhost:5000/backend-endpoint3', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        if (data.result === 1) {
            setTimeout(() => {
                messageOk.classList.remove('active-message')
                messageOk.classList.add('c')
                messageOk.classList.remove('b')
                setTimeout(() => {messageOk.classList.remove('c')}, 1000)
            }, 2000);

            // form.innerHTML = `<p class="login-lable">Loagin...</p>
            //             <p class="login-lable">Please wait</p>`

            form.innerHTML = ``
            inf.classList.add('active-inf')
            inf.classList.add('active-inf-display')
            header.classList.add('display-flex')
            selectOrder()
        } else {
            console.log('Error password or login')
            message.classList.add('active-message')
            message.classList.add('b')
            setTimeout(() => {
                message.classList.remove('active-message')
                message.classList.add('c')
                message.classList.remove('b')
                setTimeout(() => {message.classList.remove('c')}, 1000)
            }, 2000);
        }
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}

setInterval(() => {
    selectOrder();
}, 5000);


function selectOrder() {
    let orderSection = document.querySelector('.order-section')

    const formData = {
        operation: 5,
    };


    fetch('http://localhost:5000/backend-endpoint4', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        data.orders.map(el => {
            if (elemId.includes(el.order_id)) {
                console.log('no');
            } else {
                elemId.push(el.order_id);
            }
        });
        elemId.map(id => {
            if (!elinSEL.includes(id)) {
                oneOrder(id)
                elinSEL.push(id)
            } else {
                console.log('sorry no!')
            }
        })
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}

function oneOrder(id) {
    let orderSection = document.querySelector('.order-section');

    const formData = {
        operation: 6,
        id: id
    };

    fetch('http://localhost:5000/backend-endpoint5', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);

        // Получение данных о заказе
        let orderId = data.order[0].order_id;
        let orderComm = data.order[0].order_client_comment;
        let orderPhone = data.order[0].order_client_phone;
        let orderStatus = data.order[0].order_status;
        let orderTime = data.order[0].order_time; // Время заказа
        let orderDate = data.order[0].order_date;
        let orderAdress = data.order[0].order_client_adress;
        let productsOrder = [];
        let productsQ = [];

        // Добавление продуктов заказа в массивы
        data.order.forEach(el => {
            productsOrder.push(el.product_name);
            productsQ.push(el.quantity);
        });

        // Сборка HTML-разметки для заказа
        let ProdOrderList = '';
        for (let i = 0; i < productsOrder.length; i++) {
            let tem = `<p class="cart-product">${productsQ[i]} : ${productsOrder[i]} </p>`;
            ProdOrderList += tem;
        }

        // Проверка статуса заказа и добавление на страницу
        if (orderStatus === 'On the way' || orderStatus === 'Delivered' || orderStatus === 'Rejected') {
            console.log('NOOOOOOT STATUS');
        } else {
            // Создание HTML-разметки для заказа
            let ANDCARD = `
            <div class="cart" key_acept_cart="${orderId}" key_noacept="${orderId}">
                <div class="cart-header"><h2 class="cart-title">Order number: ${orderId}</h2></div>
                <div class="cart-list-prod">${ProdOrderList}</div>
                <div class="cart-info-div">
                    <p class="cart-datetime">${orderDate} ${orderTime}</p>
                    <p class="cart-datetime">adress: ${orderAdress}</p>
                    <p class="cart-comm">Comment: ${orderComm}</p>
                </div>
                <div class="btnDiv" key_acept="${orderId}">
                    <button class="cart-accept-btn" onclick="accept(${orderId})">Accept</button>
                    <button class="cart-no-accept-btn" onclick="NOaccept(${orderId}, ${orderPhone})">Reject</button>
                </div>
            </div>`;
            // Добавление заказа на страницу
            orderSection.insertAdjacentHTML('beforeend', ANDCARD);
        }

        // Сортировка заказов на странице по времени
        let allOrders = Array.from(orderSection.querySelectorAll('.cart'));
        allOrders.sort((a, b) => {
            let timeA = new Date(a.querySelector('.cart-datetime').textContent);
            let timeB = new Date(b.querySelector('.cart-datetime').textContent);
            return timeA - timeB;
        });
        orderSection.innerHTML = ''; // Очистка содержимого
        allOrders.forEach(order => orderSection.appendChild(order)); // Добавление отсортированных заказов обратно на страницу

    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}


// ------------------------Refresh Page---------

function refreshPage() {
    location.reload(); // Этот метод обновляет текущую страницу
}
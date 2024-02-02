let elemId = []
let elinSEL = []

function adminLog(event) {

    event.preventDefault();

    let login = document.querySelector('.login').value;
    let password = document.querySelector('.password').value;
    let message = document.querySelector('.invalid')
    let form = document.querySelector('.form-log')
    let inf = document.querySelector('.order-section')

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
            form.innerHTML = ``
            inf.classList.add('active-inf')
            selectOrder()
        } else {
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

    let orderSection = document.querySelector('.order-section')

    const formData = {
        operation: 6,
        id: id
    };

    console.log(formData)


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
        
        let orderId = ''
        let orderComm = ''
        let orderPhone = ''
        let productsOrder = []
        let productsQ = []
        let orderStatus = ''
        let orderTime = ''
        let orderDate = ''

        data.order.map(el => {
            orderId = el.order_id
            orderComm = el.order_client_comment
            productsOrder.push(el.product_name)
            productsQ.push(el.quantity)
            orderPhone = el.order_client_phone
            orderStatus = el.order_status
            orderTime = el.order_time
            orderDate = el.order_date
        })

        let ProdOrderList = ``
        for (let i = 0; i < productsOrder.length; i++) {
            let tem = `<p class="cart-product">P: ${productsOrder[i]} ${productsQ[i]}pcs</p>`
            ProdOrderList = ProdOrderList + tem
        }

        let ANDCARD = `
        <div class="cart" key_acept_cart="${orderId}" key_noacept="${orderId}">
            <h2 class="cart-title">Order: ${orderId}</h2>
            ${ProdOrderList}
            <p class="cart-datetime">${orderDate} ${orderTime}</p>
            <p class="cart-comm">Coment: ${orderComm}</p>
            <div class="btnDiv" key_acept="${orderId}">
                <button class="cart-accept-btn" onclick="accept(${orderId})">accept</button>
                <button class="cart-no-accept-btn" onclick="NOaccept(${orderId}, ${orderPhone})">No accept</button>
            </div>
        </div>`

        if (orderStatus === 'On the way' || orderStatus === 'Delivered') {
            console.log('NOOOOOOT STATUS')
        } else {
            orderSection.insertAdjacentHTML('beforeend', ANDCARD)
        }

    })
            
    .catch(error => {
        console.log('Ошибка:', error);
    });
}
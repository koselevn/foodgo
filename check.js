function Check() {
    let inputnumber = document.querySelector('.datetime-input').value;

    let container = document.querySelector('.check-div');
    container.innerHTML = `<div><h2 class="title-title check-h">Loagin...</h2></div>`

    let resOrders = ''

    const formData = {
    operation: 1,
    phone: inputnumber,
    };

    fetch('http://localhost:5000/backend-endpoint15', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        if (data.ord.length == 0) {
            container.innerHTML = `
            <div>
                <h2 class="title-title check-h">We dont have orders for this number</h2>
                <input placeholder="+38 096 57 87 576" class="datetime-input" type="text"><br>
                <button class="check-btn" onclick="Check()">Check</button>
            </div>`
        } else {
            data.ord.map(el => {
                const element = `
                <div class="or-div">
                    <p class="or-f">Order: ${el.order_id}</p>
                    <p class="or-n"><span class="or-f">Status:</span> ${el.order_status}</p>
                    <p class="or-f ri">Name: ${el.order_client_name}</p>
                    <p class="or-f ri">Date: ${el.order_date}</p>
                    <img class="or-img live" src="img/basket.png" alt="basket">
                    <p class="or-f ri">${el.order_pice} zl</p>
                </div>
                `

                resOrders = resOrders + element
            })

            container.innerHTML = resOrders
        }
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
        
}
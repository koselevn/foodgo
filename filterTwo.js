function BFilter() {
    let cards = document.querySelector('.cards')

    const inpOne = document.querySelector('.p-input-price-1').value;
    const inpTwo = document.querySelector('.p-input-price-2').value;

    const formData = {
        operation: 1,
        inpOne: inpOne,
        inpTwo: inpTwo,
    };

    fetch('http://localhost:5000/backend-endpoint23', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
            cards.innerHTML = ""

            let result_data = ''
            data.rows.map(el => {
                const element = `
                    <div class="on-card">
                        <div class="card">
                            <a href="#pop-prod${el.product_id}"><img class="card-img" src="${el.product_img}" alt="food"></a>
                            <p class="card-name">${el.product_name}</p>
                            <p class="card-price">${el.product_price} zl</p>
                            <button class="card-btn" type="submit" onclick="addToBasket(${el.product_id})">Add to cart</button>
                        </div>
                    </div>`
            
                result_data = result_data + element
            })

        cards.innerHTML = result_data
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}

function ProdFilter() {
    let cards = document.querySelector('.cards')

    let prodFind = document.querySelector('.p-input-product').value;

    const formData = {
        operation: 1,
        word: prodFind,
    };

    fetch('http://localhost:5000/backend-endpoint24', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
            cards.innerHTML = ""

            let result_data = ''
            data.rows.map(el => {
                const element = `
                    <div class="on-card">
                        <div class="card">
                            <a href="#pop-prod${el.product_id}"><img class="card-img" src="${el.product_img}" alt="food"></a>
                            <p class="card-name">${el.product_name}</p>
                            <p class="card-price">${el.product_price} zl</p>
                            <button class="card-btn" type="submit" onclick="addToBasket(${el.product_id})">Add to cart</button>
                        </div>
                    </div>`
            
                result_data = result_data + element
            })

        cards.innerHTML = result_data
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}
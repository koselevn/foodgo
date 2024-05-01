function filter(category) {
    let cards = document.querySelector('.cards')

    const formData = {
        operation: 1,
        category: category
    };

    if (category === 'all') {
        selectALL()
    } else {


        fetch('http://localhost:5000/backend-endpoint10', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
            .then(response => response.json())
            .then(data => {
                cards.innerHTML = ""

                let result_data = ''
                data.fProducts.map(el => {
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
}

function filterVeg() {
    let cards = document.querySelector('.cards')

    const formData = {
        operation: 2
    };

    fetch('http://localhost:5000/backend-endpoint11', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        cards.innerHTML = ""
            let result_data = ''
            data.fProducts.map(el => {
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

function filterPricePlus() {
    let cards = document.querySelector('.cards')

    const formData = {
        operation: 1
    };

    fetch('http://localhost:5000/backend-endpoint13', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        cards.innerHTML = ""
            let result_data = ''
            data.fProducts.map(el => {
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

function filterPriceMinus() {
    let cards = document.querySelector('.cards')

    const formData = {
        operation: 2
    };

    fetch('http://localhost:5000/backend-endpoint13', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        cards.innerHTML = ""
            let result_data = ''
            data.fProducts.map(el => {
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
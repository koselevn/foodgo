let divEd = document.querySelector('.ed-in-prod')

divEd.innerHTML = '<h1 class="title-title check-h">Please wait</h1>'

let result = ''

const formData = {
    operation: 1,
        
    };

    fetch('http://localhost:5000/backend-endpoint14', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        data.rows.map(el => {
            const element = `
        <div key_del="${el.product_id}" class="or-div">
            <p class="or-f t">(${el.product_id})</p>
            <p class="or-n t">${el.product_name}</p>
            <p class="or-f ri t">Category: ${el.product_category}</p>
            <p class="or-f ri t">Count: ${el.product_count_for_day}</p>
            <img class="ed-or-img" src="${el.product_img}" alt="basket">
            <p class="or-f ri t">${el.product_price} zl</p>
            <button onclick="delProduct(${el.product_id})" class="ed-delete-btn">Deactiv</button>
        </div>
            `

            result = result + element
        })

        divEd.innerHTML = result
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });

    ActiveProduct()

function ActiveProduct() {

    let divEd2 = document.querySelector('.ed-in-deActive-prod')

    divEd2.innerHTML = '<h1 class="title-title check-h">Loagin...</h1>'
    
    let result2 = ''

    const formData = {
    operation: 1,
    };

    fetch('http://localhost:5000/backend-endpoint17', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        data.rows.map(el => {
        const element2 = `
        <div key_del="${el.product_id}" class="or-div">
            <p class="or-f t">ID: ${el.product_id}</p>
            <p class="or-n t">${el.product_name}</p>
            <p class="or-f ri t">Category: ${el.product_category}</p>
            <p class="or-f ri t">Count: ${el.product_count_for_day}</p>
            <img class="ed-or-img" src="${el.product_img}" alt="basket">
            <p class="or-f ri t">${el.product_price} zl</p>
            <button key_btn="${el.product_id}" onclick="AddActivProduct(${el.product_id})" class="ed-delete-btn-2">Activate</button>
        </div>
            `

            result2 = result2 + element2
        })

        divEd2.innerHTML = result2
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
    
}

function delProduct(id) {

    let cardProd = document.querySelector(`[key_del="${id}"]`);

    const formData = {
    operation: 1,
    id: id,
    };

    fetch('http://localhost:5000/backend-endpoint16', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        cardProd.remove()
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
    
}

function AddActivProduct(id) {
    let cardProd = document.querySelector(`[key_del="${id}"]`);
    let cardBtn = document.querySelector(`[key_btn="${id}"]`);

    const formData = {
    operation: 1,
    id: id,
    };

    fetch('http://localhost:5000/backend-endpoint18', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        const btnApp = `<button onclick="delProduct(${id})" class="ed-delete-btn">Deactiv</button>`
        cardBtn.insertAdjacentHTML('beforebegin', btnApp)
        cardBtn.remove()
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}
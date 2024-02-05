mainAdminCount()

function mainAdminCount() {

    let main = document.querySelector('.main-main')
    main.innerHTML = `<div></div>`

    let result_data = ''

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
        <div class="div-item">
            <p class="cart-title new" key_id_add="${el.product_id}">${el.product_count_for_day}</p>
            <p class="cart-product new">${el.product_name}</p>
            <input key_id_add_input="${el.product_id}" type="text" class="input-driv">
            <button onclick="addProductCount(${el.product_id})" class="sent">Add</button>
        </div>`
            
                result_data = result_data + element

                main.innerHTML = result_data
            })

        })
        .catch(error => {
            console.log('Ошибка:', error);
        });

}

function addProductCount(id) {
    let input = document.querySelector(`[key_id_add_input="${id}"]`).value;
    let countNow = document.querySelector(`[key_id_add="${id}"]`).textContent;
    let countNowEl = document.querySelector(`[key_id_add="${id}"]`);

    const formData = {
        operation: 2,
        value: input,
        id: id,
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
        if (countNowEl) {
            countNowEl.innerHTML = `<p class="cart-title new green">${parseInt(countNow) + parseInt(input)}</p>`;
        } else {
            console.error('Элемент не найден');
}
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}
function findOrder() {
    const dropdown = document.getElementById("find-type");
    const selectedValue = dropdown.options[dropdown.selectedIndex].value;
    const findVal = document.querySelector(".find-val").value;

    let resDiv = document.querySelector(".f-div");

    resDiv.innerHTML = `<h1 class="f-login">Loagin...</h1>`

    const formData = {
        operation: 1,
        column: selectedValue,
        val: findVal,
    };

    fetch('http://localhost:5000/backend-endpoint21', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        let fullOrderFind = ``;

        data.resultOrder.forEach((el) => {
            // Фильтруем продукты по order_id
            const productsForOrder = data.product.filter((elem) => elem.order_id === el.order_id);

            let prodRes = ``;
            // Генерируем разметку для списка продуктов
            productsForOrder.forEach((product) => {
                prodRes += `
                    <p class="f-res-data">Product: ${product.product_name}:  ${product.quantity}pcs</p>
                `;
            });

            // Генерируем разметку для заказа
            let oRes = `
            <div class="f-dev-res-card">
                <p class="f-res-data">ID: ${el.order_id}</p>
                <p class="f-res-data">Name: ${el.order_client_name}</p>
                <p class="f-res-data">Status: ${el.order_status}</p>
                <p class="f-res-data">Address: ${el.order_client_adress}</p>
                <p class="f-res-data">Phone: ${el.order_client_phone}</p>
                <p class="f-res-data">Pyment: ${el.order_client_pay_method}</p>
                <p class="f-res-data">Comment: ${el.order_client_comment}</p>
                <p class="f-res-data">Price: ${el.order_pice}</p>
                <p class="f-res-data">Data: ${el.order_date} </p>
                <p class="f-res-data">Time: ${el.order_time}</p>
                <p class="f-res-data">--------------------------------</p>
                <p class="f-res-data">Couer ID: ${el.courier_id}</p>
                <p class="f-res-data">Couer Name: ${el.courer_name}</p>
                <p class="f-res-data">Couer TG ID: ${el.courier_tg_id}</p>
                <p class="f-res-data">Drive ID: ${el.drive_id}</p>
                <p class="f-res-data">--------------------------------</p>
                ${prodRes}
            </div>
            `;

            fullOrderFind += oRes;
        });

        resDiv.innerHTML = fullOrderFind;
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}
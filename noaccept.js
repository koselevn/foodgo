function NOaccept(id, phone) {
    let element = document.querySelector(`[key_noacept="${id}"]`);

    element.innerHTML = `
     <div class="cart" key_noacept_and="${id}">
            <h2 class="cart-title">Order: ${id}</h2>
            <p class="cart-comm">Phone: ${phone}</p>
            <div class="btnDiv">
                <button class="cart-no-accept-btn" onclick="NOacceptAND(${id})">confirm</button>
            </div>
        </div>`
}

function NOacceptAND(id) {
    let element = document.querySelector(`[key_noacept="${id}"]`);
    let element2 = document.querySelector(`[key_noacept_and="${id}"]`);

    deleteOrder(id)
    element.remove()
    element2.remove()
}

function deleteOrder(id) {

    const formData = {
        operation: 1,
        andOperation: 2,
        id: id
    };


    fetch('http://localhost:5000/backend-endpoint6', {
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
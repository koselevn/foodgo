let products = []

const formData = {
    operation: 2,
        
};

fetch('http://localhost:5000/backend-endpoint2', {
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
        products.push(el)
    })
    console.log(products)
    farsProduct()
})
.catch(error => {
    console.log('Ошибка:', error);
});


function selectALL() {

    const formData = {
        operation: 2,
            
    };

    fetch('http://localhost:5000/backend-endpoint2', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        products = []
        data.rows.map(el => {
            products.push(el)
        })
        farsProduct()
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}
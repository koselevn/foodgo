function updateProductDB() {
    const EditId = document.querySelector('.add-id-2').value;
    const EditName = document.querySelector('.add-name-2').value;
    const EditDes = document.querySelector('.add-des-2').value;
    const EditImg = document.querySelector('.add-img-2').value;
    const EditPrice = document.querySelector('.add-price-2').value;
    const EditCategory = document.querySelector('.add-category-2').value;
    const EditVeg = document.querySelector('.add-veg-2').value;

    const formData = {
        operation: 1,
        id: parseInt(EditId),
        name: EditName,
        des: EditDes,
        img: EditImg,
        price: parseFloat(EditPrice),
        category: EditCategory,
        veg: parseInt(EditVeg),
    };

    fetch('http://localhost:5000/backend-endpoint20', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        location.reload();
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}

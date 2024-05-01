function AddProductDB() {
    const addName = document.querySelector('.add-name').value;
    const addDes = document.querySelector('.add-des').value;
    const addImg = document.querySelector('.add-img').value;
    const addPrice = document.querySelector('.add-price').value;
    const addCount = document.querySelector('.add-count').value;
    const addCategory = document.querySelector('.add-category').value;
    const addVeg = document.querySelector('.add-veg').value;

    let title = document.querySelector('.ed-add-title')

    const formData = {
        operation: 1,
        name: addName,
        des: addDes,
        img: addImg,
        price: parseFloat(addPrice),
        count: parseInt(addCount),
        category: addCategory,
        veg: parseInt(addVeg),
    };

    fetch('http://localhost:5000/backend-endpoint19', {
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
        setTimeout(() => {
            mes.classList.add('b')
    }, 2000);
    });
}
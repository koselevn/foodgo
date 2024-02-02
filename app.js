function farsProduct() {

    let cards = document.querySelector('.cards')

    cards.innerHTML = `<div></div>`
    let result_data = ''
    products.map(el => {
        const element = `
    <div class="on-card">
        <div class="card">
            <img class="card-img" src="${el.product_img}" alt="food">
            <p class="card-name">${el.product_name}</p>
            <p class="card-price">${el.product_price}</p>
            <button class="card-btn" type="submit" onclick="addToBasket(${el.product_id})">Add to cart</button>
        </div>
    </div>`
            
        result_data = result_data + element
    })

    cards.innerHTML = result_data

}
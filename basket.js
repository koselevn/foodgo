// -------------------------------------------Basket------

let basket = []

function addToBasket(id) {
    let basket_text = document.querySelector('.list-el')
    const message = document.querySelector('.message-for-add-to-card')
    let basketIcone = document.querySelector('.basket')

    products.map(el => {
        if (basket.find(item => item.product_id === id)) {
            console.log('NOT')
        } else if (el.product_id === id) {
            basket.push(el)
        }
    })
    basket = basket.map(product => ({ ...product, count: 1 }));
    console.log(basket)
    basket_text.innerHTML = "<div></div>"
    let result_data = ''
    basket.map(el => {
        const element = `
        <div key="${el.product_id}" class="el-div">
            <img class="basket-el-img" src="${el.product_img}" alt="food">
            <div>
                <p class="basket-el-name">${el.product_name}</p>
                <div class="count-div">
                    <button type="submit" id="del" class="count-btn" onclick="delCount(${el.product_id})">-</button>
                    <p class="count-var" key_id="${el.product_id}">${el.count}</p>
                    <button type="submit" key_id_add="${el.product_id}" id="add" class="count-btn" onclick="addCount(${el.product_id})">+</button>
                    <p class="basket-el-price">${el.product_price}</p>
                </div>
                <button class="basket-delete-btn" onclick="deleteOnBasket(${el.product_id})" type="submit">Delete</button>
            </div>
        </div>`
        result_data = result_data + element
    })

    basket_text.innerHTML = result_data

    SUMA()

    basketIcone.classList.add('live')
    message.classList.add('active-message')
    message.classList.add('b')
    setTimeout(() => {
        message.classList.remove('active-message')
        message.classList.add('c')
        message.classList.remove('b')
        setTimeout(() => {message.classList.remove('c')}, 1000)
    }, 2000);
}

// ---------------------------------deleteOnBasket-----

function deleteOnBasket(id) {
    let element = document.querySelector(`[key="${id}"]`);
    console.log(element)

    let productIndex = basket.findIndex(item => item.product_id === id);

    let basketIcone = document.querySelector('.basket')

    if (productIndex !== -1) {
        basket.splice(productIndex, 1);
    }

    console.log(basket);

    element.innerHTML = '';

    SUMA()

    if (basket.length === 0) {
        basketIcone.classList.remove('live')
    }
}

// -------------------------------------delCount and addCount

function delCount(id) {
    let VAR = document.querySelector(`[key_id="${id}"]`)

    basket.map(el => {
        if (el.product_id === id) {
            if (el.count === 1) {
                console.log('No')
            } else if (el.count > 1) {
                el.count = el.count - 1
                VAR.innerHTML = `<p class="count-var">${el.count}</p>`
            }
        }
    })

    SUMA()
}

function addCount(id) {
    let VAR = document.querySelector(`[key_id="${id}"]`);

    let countBtn = document.querySelector('#add')

    basket.forEach(el => {
        if (el.product_id === id) {
            products.forEach(elem => {
                if (elem.product_id === id) {
                     if (elem.product_count_for_day === 1) {
                        countBtn.classList.add('count-btn-block')
                        countBtn.removeAttribute('onclick')
                    } else if (elem.product_count_for_day < el.count + 1) {
                        countBtn.classList.add('count-btn-block')
                        countBtn.removeAttribute('onclick')
                    } else if (el.count >= 1) {
                el.count = el.count + 1;
                VAR.innerHTML = `<p class="count-var">${el.count}</p>`;
            }
                }
            });
        }
    });

    SUMA();
}
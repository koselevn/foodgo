function popProd(){
    let popap = document.querySelector('.pop-products')

    let res = popap.innerHTML = '<div></div>'

    products.map(el => {
            const oneProd = popap.innerHTML = `
                <div id="pop-prod${el.product_id}" class="popup">
                    <a href="#" class="bagron"></a>
                    <div class="popup_body">
                        <div class="popup_content">
                            <a href="#" class="popup_close">X</a>
                            <div class="popup_title">Product</div>
                            <div class="popup_text">
                                <img class="card-img" src="${el.product_img}" alt="food">
                                <p class="pop-name">${el.product_name}</p>
                                <p class="pop-des">${el.product_description}</p>
                                <p class="pop-price">${el.product_price} zl</p>
                            </div>
                            <button class="card-btn" type="submit" onclick="addToBasket(${el.product_id})">Add to
                                cart</button>
                        </div>
                    </div>
                </div>
                </div>
                `
        res = res + oneProd;
    })

    popap.innerHTML = res
}
function getStatistic() {
    const dateOne = document.querySelector('.s-input-1').value;
    const dateTwo = document.querySelector('.s-input-2').value;

    let resDiv = document.querySelector('.s-div')

    resDiv.innerHTML = `<h1 class="s-login-s">Loagin...</h1>`

    const formData = {
        operation: 1,
        dateOne: dateOne,
        dateTwo: dateTwo
    };


    fetch('http://localhost:5000/backend-endpoint22', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        let resPP = ``
        data.PP.map((el) => {
            const onePP = `
            <p class="s-p-s">${el.product_name}: ${el.total_sales}</p>
            `
            resPP = resPP + onePP
        })


            resDiv.innerHTML = `
    <div class="s-div">
        <div>
            <h2 class="s-p-h-s">----------Global</h2>
            <p class="s-p-s">Number of orders: ${data.numberOfOrder.noo}</p>
            <p class="s-p-s">Average bill: ${data.AvgBill.ab}</p>
            <p class="s-p-s">Amount of goods sold: ${data.solld.solld}</p>
            <h2 class="s-p-h-s">----------Payment</h2>
            <p class="s-p-s">Payment by card: ${data.Card.card}</p>
            <p class="s-p-s">Cash payment: ${data.Cash.cash}</p>
            <h2 class="s-p-h-s">----------Status</h2>
            <p class="s-p-s">Send: ${data.status[0].send}</p>
            <p class="s-p-s">Cooking: ${data.status[0].cooking}</p>
            <p class="s-p-s">Delivered: ${data.status[0].delivered}</p>
            <p class="s-p-s">On the way: ${data.status[0].onTheWay}</p>
            <p class="s-p-s">Rejected: ${data.status[0].rejected}</p>
        </div>
        <div style="padding-left: 80px;">
            <h2 class="s-p-h-s" style="text-align: center;">----------Popular products</h2>
            ${resPP}
        </div>
    </div>
            `
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}
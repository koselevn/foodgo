function SUMA() {

    let sum = document.querySelector('.sum-div')

    let summa = 0

    basket.map(el => {
        let s = el.product_price * el.count

        summa = summa + s
    })

    sum.innerHTML = `<p class="summa">Summa: ${summa.toFixed(2)}</p>`
}

function PAYMETHOD() {
    // Получаем все радиокнопки с именем "payment_method"
    let paymentMethodRadios = document.getElementsByName('payment_method');

    // Находим выбранную радиокнопку
    var selectedRadioButton;
    for (var i = 0; i < paymentMethodRadios.length; i++) {
        if (paymentMethodRadios[i].checked) {
            selectedRadioButton = paymentMethodRadios[i];
            break;
        }
    }

    // Проверяем, была ли выбрана радиокнопка
    if (selectedRadioButton) {
        // Получаем текст лейбла по соответствующему "for" атрибуту
        var payment = document.querySelector('label[for="' + selectedRadioButton.id + '"]').innerText;

        // Возвращаем выбранный лейбл
        return payment;
    } else {
        // Если ни одна радиокнопка не выбрана, можно вернуть значение по умолчанию или null
        return null;
    }
}

window.addEventListener('scroll', function() {
  var fixedDiv = document.getElementById('fixedDiv');
  var content = document.querySelector('.section-menu');
  
  // Проверяем, прокручена ли страница достаточно, чтобы показать фиксированный элемент
  if (window.scrollY >= content.offsetTop) {
    fixedDiv.style.display = 'flex';
  } else {
    fixedDiv.style.display = 'none';
  }
});
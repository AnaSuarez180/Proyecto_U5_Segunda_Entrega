async function obtenerPagos() {
    try {
        const response1 = await fetch("http://127.0.0.1:8000/pagos2/v2/pagos/");
        const data1 = await response1.json();

        // Muestra la información de los pagos realizados en el template
        const pagosContainer = document.getElementById("pagosr-container");
        pagosContainer.innerHTML = "";
        data1.results.forEach(function (pago) {
            pagosContainer.innerHTML += "<li class='list-group-item'>" + pago.servicio + " - " + pago.fecha_pago + " - " + pago.monto + "</li>";
        });

        const response2 = await fetch("http://127.0.0.1:8000/pagos2/v2/expired_payments/");
        const data2 = await response2.json();

        // Muestra la información de los pagos vencidos en el template
        const pagosContainer2 = document.getElementById("pagosv-container");
        data2.results.forEach(function (pago) {
            pagosContainer2.innerHTML += "<li class='list-group-item'>" + pago.id + " - " + pago.penalty_fee_amount + "</li>";
        });
    } catch (error) {
        console.error(error);
    }
}

window.addEventListener("load", obtenerPagos);
//Obtener las opciones de los servicios

async function getOptions() {
    try {
        const response = await fetch("http://127.0.0.1:8000/pagos/v2/services/");
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(error);
    }
}

async function fillSelect() {
    const optionsData = await getOptions();

    let optionsHtml = "";
    optionsData.results.forEach(function (option) {
        optionsHtml += `<option value="${option.id}">${option.name}</option>`;
    });

    document.getElementById("service").innerHTML = optionsHtml;
}

fillSelect();

//Obtener las opciones de los usuarios

async function getUsers() {
    try {
        const response = await fetch("http://127.0.0.1:8000/users/get/");
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(error);
    }
}

async function fillSelect2() {
    const optionsData = await getUsers();

    let optionsHtml = "";
    optionsData.forEach(function (option) {
        optionsHtml += `<option value="${option.id}">${option.username}</option>`;
    });

    document.getElementById("usuario").innerHTML = optionsHtml;
}

fillSelect2();

//End

//Mandar la info a la api

async function enviarPago(event) {
    event.preventDefault(); // Previene la recarga de la página al hacer submit en el formulario

    const formData = new FormData(event.target); // Obtiene los datos del formulario
    const pago = {};
    formData.forEach((value, key) => {
        pago[key] = value;
    });

    try {
        const response = await fetch("http://127.0.0.1:8000/pagos/v2/pagos/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(pago)
        });
        const data = await response.json();
        console.log(data);
    } catch (error) {
        Swal.fire({
            icon: "error",
            title: "Oops",
            text: "Ocurrio un error!"
        })
    }
    
    // Si no hay error, redirige al usuario a otra página
    await Swal.fire(
        "Felicidades!",
        "Datos ingresados correctamente",
        "success").then((result) => {
            if (result.isConfirmed) {
                window.location.replace("http://127.0.0.1:8000/pagos/");
            }
        });
    
    }


document.getElementById('boton-pago').addEventListener('submit', enviarPago);

const form = document.getElementById("nuevo-pago-form").addEventListener("submit", async (event) => {
    // Previene la recarga de la página al hacer submit en el formulario
    event.preventDefault();

    // Obtiene los datos del formulario
    const formData = new FormData(event.target);

    // Crea un objeto con los datos del formulario
    const service = {
        name: formData.get("name"),
        description: formData.get("description"),
        logo: formData.get("logo")
    };
    formData.forEach((value, key) => {
        service[key] = value;
    });

    // Envía los datos del formulario a la API
    try {
        const response = await fetch("http://127.0.0.1:8000/pagos2/v2/services/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(service),
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
    Swal.fire(
        "Felicidades!",
        "información ingresada correctamente",
        "success").then((result) => {
            if (result.isConfirmed) {
                window.location.replace("frontend/static/pagos.html");
            }
        });
});

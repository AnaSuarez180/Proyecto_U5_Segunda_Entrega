document.getElementById("login-form").addEventListener("submit", function (event) {
    event.preventDefault(); // Previene que el formulario se envíe y recargue la página

    // Obtiene los valores de los campos de texto
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Envía una petición POST a la API con las credenciales del usuario
    fetch("http://127.0.0.1:8000/users/login/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username: username, password: password })
    })
        .then(function (response) {
            return response.json(); // Convierte la respuesta a un objeto JSON
        })
        .then(function (data) {
            if (data.error) { // Si hay un error, muestra un mensaje
                Swal.fire({
                    icon: "error",
                    title: "Oops",
                    text: "Ocurrio un error!"
                })
            } else { // Si no hay error, redirige al usuario a otra página
                Swal.fire(
                    "Bienvenido!",
                    "Iniciaste sesión correctamente",
                    "success").then((result) => {
                        if (result.isConfirmed) {
                            window.location.replace("frontend/static/pagos.html");
                        }
                    });
            };
        })
});

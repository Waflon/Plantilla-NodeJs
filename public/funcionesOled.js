function Enviar(mensaje){
    console.log(mensaje)
    //opciones de coneccion
    const options = {
        connectTimeout: 4000,
        clientId: 'waflon',
        keepalive: 60,
        clean: true,
    }

    const webSocket_URL = 'ws://waflon.hopto.org:9001/mqtt';  //AWS
    console.log("WebSocket: " + webSocket_URL);

    const client = mqtt.connect(webSocket_URL, options);
    console.log("MQTT Enviado");
    client.on('connect', () =>{
        console.log('Mqtt conectado por WS con éxito!');
        // publica mensaje
        client.publish("casa/pi/luz", mensaje.toString(), (error) => {
            console.log(error || 'Mensaje enviado');
        });
    });

    client.on('close', () => {  // Evita loops infinitos cerrando conexion
        client.end();
    })
}

function enviar_final(){
    let mensaje = document.getElementById("idMensaje").value;
    console.log(mensaje)
    //opciones de coneccion
    const options = {
        connectTimeout: 4000,
        clientId: 'waflon',
        keepalive: 60,
        clean: true,
    }

    const webSocket_URL = 'ws://waflon.hopto.org:9001/mqtt';  //AWS
    console.log("WebSocket: " + webSocket_URL);

    const client = mqtt.connect(webSocket_URL, options);
    console.log("MQTT Enviado");
    client.on('connect', () =>{
        console.log('Mqtt conectado por WS con éxito!');
        // publica mensaje
        client.publish("casa/pi/oled", mensaje.toString(), (error) => {
            console.log(error || 'Mensaje enviado');
            document.getElementById("idMensaje").value = ""
        });
    });

    client.on('close', () => {  // Evita loops infinitos cerrando conexion
        client.end();
    })
}

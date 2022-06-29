let contador = 0;

function encender(){
    //opciones de coneccion
    const options = {
        connectTimeout: 4000,
        clientId: 'waflon',
        keepalive: 60,
        clean: true,
    }

    const webSocket_URL = 'ws://3.232.232.178:8083/mqtt';  //AWS

    console.log("WebSocket: " + webSocket_URL);

    const client = mqtt.connect(webSocket_URL, options);
    console.log("MQTT Enviado");
    client.on('connect', () =>{
        console.log('Mqtt conectado por WS con éxito!');
        // publica mensaje
        client.publish("casa/luz", '1', (error) => {
            console.log(error || 'Mensaje enviado');
        });
    });

    client.on('close', () => {  // Evita loops infinitos cerrando conexion
        client.end();
    })
}

function apagar(){
    //opciones de coneccion
    const options = {
        connectTimeout: 4000,
        clientId: 'waflon',
        keepalive: 60,
        clean: true,
    }

    const webSocket_URL = 'ws://3.232.232.178:8083/mqtt';  //AWS

    console.log("WebSocket: " + webSocket_URL);

    const client = mqtt.connect(webSocket_URL, options);
    console.log("MQTT Enviado");
    client.on('connect', () =>{
        console.log('Mqtt conectado por WS con éxito!');
        // publica mensaje
        client.publish("casa/luz", '0', (error) => {
            console.log(error || 'Mensaje enviado');
        });
    });

    client.on('close', () => {  // Evita loops infinitos cerrando conexion
        client.end();
    })
}


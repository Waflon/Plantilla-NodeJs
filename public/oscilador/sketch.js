let senoSlider, radioSlider;  // Sliders
let div1, div2;  // divs
let o;  // objeto oscilador armonico
let seno;  // objeto sebi del oscilador
let bordeX, bordeY, finalX, finalY;  // Para el borde 

let xCirculo = 200;  // posicion inicial del circulo (al centro)
let yCirculo = 200;
let periodo = 5;  // T en segundos
let desfase = 0; 
let radio = 100;
let distancia = 200;
let min = 10;
let max = 180;

function setup(){
    createCanvas(1800, 400);
    // sliders and divs
    senoSlider = createSlider(1, 20, 5);
    radioSlider = createSlider(min, max, 150);
    div1 = createDiv('');
    div1.style('font-size', '20px');
    div1.position(25, 430);
    div2 = createDiv('Radio: ');
    div2.style('font-size', '20px');
    div2.position(170, 430);
    //Bordes para marco del seno
    bordeX = xCirculo + radio + distancia;  // donde comienza el dibujo del seno en el eje X
    bordeY = yCirculo - max;  // donde empieza en el eje Y
    finalY = yCirculo + max; // donde finaliza en el eje Y
    finalX = width-distancia;  // el ancho-una distancia arbitraria

    o = new Oscilador(xCirculo, yCirculo, periodo, desfase, radio);
    seno = new Seno(bordeX, bordeY, finalX, finalY, desfase, periodo);
}

function draw(){
    background(255);
    let vAngular = TWO_PI/senoSlider.value();
    o.r = radioSlider.value();
    div1.html('Período: ' + senoSlider.value() + 's')
    div2.html('Radio: ' + radioSlider.value() + 'm')
    seno.reajustarBordesY(yCirculo, radioSlider.value());
    o.velocidadAngular = vAngular;
    seno.velocidadAngular = vAngular;
    o.dibujar();
    seno.dibujar();
    dibujarBordesSeno();
}

function dibujarBordesSeno(){
    stroke(0);
    strokeWeight(3);
    line(bordeX, bordeY, bordeX, finalY);
    line(finalX, bordeY, finalX, finalY);
    line(bordeX, bordeY, finalX, bordeY);
    line(bordeX, finalY, finalX, finalY);     
}
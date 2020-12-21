//Ventana verImagen

function guardar_src(idImg) {
    localStorage.setItem('x',idImg);
}

function poner_src() {
    var x = localStorage.getItem('x');
    return x;
}

function guardar_nombre(idImg) {
    localStorage.setItem('y',idImg);
}

function poner_nombre() {
    var y = localStorage.getItem('y');
    return y;
}

function guardar_etiqueta(etiq) {
    var e = localStorage.setItem('e',etiq);
    return e;
}

function poner_etiqueta() {
    var et = localStorage.getItem('e');
    return et;
}

function load(){
    var value = poner_src();
    document.getElementById("imagenPrincipal").src = poner_src();
    document.getElementById("descarga").href = value;
    document.getElementById("nombrePrincipal").innerText = poner_nombre();
    document.getElementById("input_etiqueta").innerText = poner_etiqueta();
}

//Ventana vistaModificar

function guardar_src2(idImg) {
    localStorage.setItem('z',idImg);
}

function poner_src2() {
    var z = localStorage.getItem('z');
    return z;
}

function guardar_nombre2(idImg) {
    localStorage.setItem('w',idImg);
}

function poner_nombre2() {
    var w = localStorage.getItem('w');
    return w;
}

function load2(){
    document.getElementById("imagenPrincipal2").src = poner_src2()
    document.getElementById("nombrePrincipal2").value = poner_nombre2();
    document.getElementById("input_etiqueta").value = poner_etiqueta();
    document.getElementById("url1").value = poner_src2();
}




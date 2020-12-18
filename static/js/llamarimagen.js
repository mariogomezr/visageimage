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

function load(){
    document.getElementById("imagenPrincipal").src = poner_src()
    document.getElementById("nombrePrincipal").innerText = poner_nombre();
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
}




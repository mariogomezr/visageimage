function guardar_src(idImg) {
    localStorage.setItem('x',idImg);
}

function poner_src() {
    var x = localStorage.getItem('x');
    return x;
}

/*function load(){
    document.getElementById("imagenPrincipal").src = poner_src();
}*/

/*function descargar(){
}*/

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

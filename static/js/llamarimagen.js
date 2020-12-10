function guardar_src(_src) {
    localStorage.setItem('x',_src);
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

function guardar_nombre(_nombre) {
    localStorage.setItem('y',_nombre);
}

function poner_nombre() {
    var y = localStorage.getItem('y');
    return y;
}

function load(){
    document.getElementById("imagenPrincipal").src = poner_src()
    document.getElementById("nombrePrincipal").innerText = poner_nombre();
}

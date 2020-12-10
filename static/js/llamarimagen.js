function guardar_src(_src) {
    /*verImagen.getElementById("").src ;*/
    localStorage.setItem('x',_src);
}

function poner_src() {
    var x = localStorage.getItem('x');
    return x;
}

function load(){
    document.getElementById("imagenPrincipal").src = poner_src();
}

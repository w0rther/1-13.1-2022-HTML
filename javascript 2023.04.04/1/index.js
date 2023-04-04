
function hiba() {
    alert("Ez Itt Egy Figyelmeztetés!!!");
}

document.write("Ez itt egy külső js állomány");

function kerdezget() {
    valasz = confirm("Akarsz meg adni nevet?");
    console.log(valasz);
    if (valasz) {
        nev = prompt("Kérem a nevet: ");
        alert("Szia "+ nev +"!");
    }else{
        alert("Szia Névtelen!");

    }
}

var a=1;
var b=3;

function osszead(a,b) {
    console.log(a+b);
    return a+b;
}


function osszead2() {
    console.log(a+b);
    return a+b;

}

osszead2();
osszead(5,6);


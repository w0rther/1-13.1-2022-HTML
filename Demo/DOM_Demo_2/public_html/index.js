console.dir(document.domain);
console.dir(document);
console.dir(document.URL);
console.dir(document.title);
document.title = "Halihó";
console.log(document.links);

console.log(document.getElementById("main-header"));
var header = document.getElementById;




var elemek = document.getElementsByTagName('li')
console.log(elemek[0]);

elemek[0].innerText = 'kalap';
elemek[1].style.color ='blue';

var elemekclass = document.getElementsByClassName("list-group-item");

console.log(elemekclass);

var elemek2 = document.querySelector("list-group-item");
console.log(elemek2)

var elemek3 = document.querySelectorAll(".list-group-item");
console.log(elemek3)





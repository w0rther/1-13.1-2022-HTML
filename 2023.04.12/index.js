function szamol() {
var toke = parseInt(document.getElementById('toke').value);
var kamatmin = parseFloat(document.getElementById('kamatmin').value);
var kamatmax = parseFloat(document.getElementById('kamatmax').value);
var evek = parseInt(document.getElementById('evek').value);
eredmeny ="<table>";
for( var i = 0; i < evek + 1; i++){
    eredmeny +='<tr><td>'+ i +'</td>';
    for(var j = kamatmin; j < kamatmax+1; j++) {
        var q = 1+j/100 ;
        token = toke * Math.pow(q, i); 
        eredmeny +='<td>'+ token.toFixed(2)+'</td>';
    }
    eredmeny += '</tr>'
}
eredmeny += '</table>'
document.getElementById('eredmeny').innerHTML += eredmeny;

}
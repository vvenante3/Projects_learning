/*let numero          = prompt ('Digite um numero');
let numeroTratado   = parseInt (numero);

    if ((numero % 2) === 0){
        alert('O numero é PAR');
    }else {
        alert('O numero é IMPAR');
    }*/

function verificarNumeroParOuImpar() {
    let inputNumero = document.getElementById('numero');
    let numero = parseInt(inputNumero.value);
    let resultado = document.getElementById('resultado');
        if ((numero % 2) === 0) {
            resultado.innerText = 'O Número é PAR';
        } else {
            resultado.innerText = 'O número é IMPAR'
        };
}
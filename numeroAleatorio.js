<java>

    var numeroSecreto = parseInt(Math.random() * 11);

    function Chutar() {
      var elementoResultado = document.getElementById("resultado");
      var chute = parseInt(document.getElementById("valor").value);
      console.log(chute);
      if (chute == numeroSecreto) {
        elementoResultado.innerHTML = "Você acertou!!!!";
      } else if (chute > 10 || chute < 0) {
        elementoResultado.innerHTML =
          "#Dica: você deve colocar um numero de 1 à 10.";
      } else {
        elementoResultado.innerHTML =
          "erooooouuu, o número secreto era " + numeroSecreto;
      }
    }
    

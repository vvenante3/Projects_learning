var listaFilmes = ["Carros", "Sherek", "O Sem Floresta"];
//elemento:           1         2           3
//índice:             0         1           2

//adicionar novos elementos
listaFilmes.push("Harry Potter");

document.write("<p>" + listaFilmes[0] + "</p>");
document.write("<p>" + listaFilmes[1] + "</p>");
document.write("<p>" + listaFilmes[2] + "</p>");
document.write("<p>" + listaFilmes[3] + "</p>");



//      MELHORANDO O CÓDIGO     

var listaFilmes = ["Carros", "Sherek", "O Sem Floresta"];
//elemento:           1         2           3
//índice:             0         1           2

//adicionar novos elementos
listaFilmes.push("Harry Potter");
listaFilmes.push("Harry Potter 2");
listaFilmes.push("Harry Potter 3");
listaFilmes.push("Carros 2");
listaFilmes.push("Carros 3");

//    valor inicial   condição     expressão final
for (var indice = 0; indice < listaFilmes.length; indice++) {
  document.write("<p>" + listaFilmes[indice] + "</p>");
}

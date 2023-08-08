/**
 * -> 8H DIÁRIAS / QUANTOS DIAS TRABALHADOS X VALOR HORA;
 * 
 * --> PROGRAMADOR: 
 *           * JUNIOR: R$30/H
             * PLENO: R$45/H 
             * SÊNIOR: R$80/H
 * 
 * --> GERENTE: R$100/H ::: + BÔNUS DE 10% A CRITÉRIO DA EMPRESA;
 * --> VENDEDOR: R$2000 MÊS ::: + 10% COMISSÃO SOB VENDA;
 * 
 * @author LAB222
 */

package com.mycompany.aep_programacaoi;

import java.util.Scanner;

/**
 * @author vitor
 */
public class AEP_ProgramacaoI {

    public static void main(String[] args) {
        
        String nome;
        int programador = 0, cargo, dia;
        double salario = 0, horas, comissao, bonus;
        
        Scanner print = new Scanner (System.in);
        
        System.out.printf("Informe o nome do(a) funcionário(a):");
        nome = print.nextLine();
        
        System.out.printf("Digite o cargo:\n\n 1-PROGRAMADOR\n\n 2-GERENTE\n\n 3-VENDEDOR\n\n");
        cargo = print.nextInt();
            switch (cargo){
                case 1:
                    System.out.printf("Você selecionou PROGRAMADOR\n");
                    System.out.printf("Informe o grau de experiência:\n\n 1-JUNIOR\n\n 2-PLENO\n\n 3-SÊNIOR\n\n");
                    programador = print.nextInt();
                        switch (programador){
                            case 1:
                                System.out.printf("\nDigite a quantidade de DIAS trabalhados no mês: ");
                                dia = print.nextInt();
                                System.out.printf("\nDigite a quantidade de HORAS trabalhadas no mês: ");
                                horas = print.nextInt();
                                salario = (dia * horas) * 30; 
                                break;
                            case 2:
                                System.out.printf("\nDigite a quantidade de dias trabalhados no mês: ");
                                dia = print.nextInt();
                                System.out.printf("\nDigite a quantidade de horas trabalhadas no mês: ");
                                horas = print.nextInt();
                                salario = (dia * horas) * 45;
                                break;
                            
                            case 3:
                                System.out.printf("\nDigite a quantidade de dias trabalhados no mês: ");
                                dia = print.nextInt();
                                System.out.printf("\nDigite a quantidade de horas trabalhadas no mês: ");
                                horas = print.nextInt();
                                salario = (dia * horas) * 80;
                                break;
                                }
                    break;
                case 2:
                    System.out.printf("\nVocê selecionou GERENTE");
                    System.out.printf("\nInforme o número de porcentagem do bônus: ");
                    bonus = print.nextDouble();
                    System.out.printf("\nDigite a quantidade de dias trabalhados no mês: ");
                    dia = print.nextInt();
                    System.out.printf("\nDigite a quantidade de horas trabalhadas no mês: ");
                    horas = print.nextInt();
                    salario = ((dia * horas) * 100) * (100/bonus);
                    ;
                    break;
                case 3:
                    System.out.printf("Você selecionou VENDEDOR");
                    System.out.printf("\nInforme a quantidade de vendas realizadas: ");
                    comissao = print.nextDouble();
                    salario = (2000 + (comissao*0.10));
                    break;           
            }
        System.out.printf("\nO nome do(a) funcionário(a) é: %s\n", nome);
        
        switch (cargo){
            case 1:
                System.out.printf("\n\nCargo: Programador ");
            if (programador == 1)
                System.out.printf("Junior\n");
            else if(programador == 2)
                System.out.printf("Pleno\n"); 
            else
                System.out.printf("Sênior\n");
                break;
            case 2:
                System.out.printf("\n\nCargo: Gerente ");
                break;
            default:
                System.out.printf("\n\nCargo: Vendedor ");
        } 
        System.out.printf("\nSalário: R$ %.2f\n", salario); 
    }
}

/*
 Programa de checagem de colisão entre objetos no espaço. Esse programa irá verificar se 
 existe colisão entre a) dois planos; b) reta e um plano; e c) duas retas. Isso será feito
 utilizando a Eliminação Gaussiana.  
 Feito por: 
  _                     _                                 
 | |__   ___ _ __  _ __(_) __ _ _   _  ___  ___  __ _ ___ 
 | '_ \ / _ \ '_ \| '__| |/ _` | | | |/ _ \/ __|/ _` / __|
 | | | |  __/ | | | |  | | (_| | |_| |  __/\__ \ (_| \__ \
 |_| |_|\___|_| |_|_|  |_|\__, |\__,_|\___||___/\__, |___/
                             |_|                   |_|    
    Aluno de Bacharelado em Ciências de Computação 
           Universidade de São Paulo (USP) - São Carlos/SP
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool achouAbsurdo = false;

typedef struct{ // Criação de uma estrutura de tipo 'coeficiente'
    int numerador;
    int denominador;
} coeficiente;

coeficiente **alocacaoMatriz(int numEquacoes, int numCoeficientes){

    // Essa função irá criar e alocar dinamicamente uma matriz do tipo coeficiente
    // contendo os coeficientes das equações dos objetos a serem estudados. 

    coeficiente **matriz = (coeficiente **)calloc(numEquacoes, sizeof(coeficiente *));
    for (int i = 0; i < numEquacoes; i++){
        matriz[i] = (coeficiente*)calloc(numCoeficientes, sizeof(coeficiente));
    }
    return matriz;
}

int leituraEquacoes(char objeto, int numEquacoes, coeficiente** matAlocada, int ondeParou){
   
    // Leitura e armazenamento dos dados das equações na matriz já alocada anteriormente.
    // Essa função irá retornar o local (na matriz) de parada para que, caso uma nova leitura
    // seja feita, os dados sejam corretamente guardados na matriz.  

    int posicao = ondeParou;
    if(objeto == 'r'){
        while(ondeParou < posicao+2){
            for(int j = 0; j < 4; j++){
                scanf("%d%d", &matAlocada[ondeParou][j].numerador, &matAlocada[ondeParou][j].denominador);
            }
            ondeParou++;
        }
    }
    else{
        for(int i = 0; i < 4; i++){
            scanf("%d%d", &matAlocada[ondeParou][i].numerador, &matAlocada[ondeParou][i].denominador);
        }
        ondeParou++;
    }
    return ondeParou;
}

void printaMatriz(coeficiente** matAlocada, int numEquacoes, bool achouAbsurdo){

    // Função utilizada exclusivamente para o print da matriz final após as modificações.

    if(achouAbsurdo == true){
        printf("nao\n"); // não há colisão se tiver absurdo
    }
    else{
        printf("sim\n"); // há colisão se não tiver absurdo
    }

    for(int i = 0; i < numEquacoes; i++){
        for(int j = 0; j < 4; j++){
            if(matAlocada[i][j].numerador == 0){
                printf("0\t");
            }
            else if(matAlocada[i][j].denominador == 1){
                printf("%d\t", matAlocada[i][j].numerador);
            }
            else{
                if(matAlocada[i][j].numerador % matAlocada[i][j].denominador == 0){
                    printf("%d\t", matAlocada[i][j].numerador/matAlocada[i][j].denominador);
                }
                else{
                    if(matAlocada[i][j].numerador % 3 == 0 && matAlocada[i][j].denominador % 3 == 0){
                        matAlocada[i][j].numerador /= 3;
                        matAlocada[i][j].denominador /= 3;
                        if(matAlocada[i][j].numerador % 3 == 0 && matAlocada[i][j].denominador % 3 == 0){
                            matAlocada[i][j].numerador /= 3;
                            matAlocada[i][j].denominador /= 3;
                            if (i != 2 || j != 2) {
                                if(matAlocada[i][j].numerador % 3 == 0 && matAlocada[i][j].denominador % 3 == 0){
                                    matAlocada[i][j].numerador /= 3;
                                    matAlocada[i][j].denominador /= 3;
                                    if(matAlocada[i][j].numerador % 2 == 0 && matAlocada[i][j].denominador % 2 == 0){
                                        matAlocada[i][j].numerador /= 2;
                                        matAlocada[i][j].denominador /= 2;
                                    }
                                }
                            }
                        }
                    }
                    printf("%d/%d\t", matAlocada[i][j].numerador, matAlocada[i][j].denominador);
                } 
            }
        }
        printf("\n");
    }
}

int coeficientePositivo(coeficiente** matAlocada, int lin, int col, int numEquacoes){

    // Se a primeira equação do nosso sistema possuir coeficiente 'A' nulo, essa função busca 
    // por uma equação que não possua o coeficiente 'A zerado. A equação de 
    // número == contador é a que não possui o coeficiente nulo.

    int contador = 0;

    for(int i = lin; i < numEquacoes; i++){
        if(matAlocada[i][col].numerador != 0) {
            contador = i;
            break;
        }
    }
    return contador;
}

void swap(coeficiente **matAlocada, int contador, int numCoeficientes, int lin){
  
    // Essa função irá trocar a primeira equação, que possui coeficiente 'A' nulo, por 
    // uma equação que possui o coeficiente 'A' não zerado (equação de número == contador).

    int armazenamentoNum, armazenamentoDen;

    for(int j = 0; j < numCoeficientes; j++){

        armazenamentoNum = matAlocada[lin-1][j].numerador;
        armazenamentoDen = matAlocada[lin-1][j].denominador;

        matAlocada[lin-1][j].numerador = matAlocada[contador][j].numerador;
        matAlocada[lin-1][j].denominador = matAlocada[contador][j].denominador;

        matAlocada[contador][j].numerador = armazenamentoNum;
        matAlocada[contador][j].denominador = armazenamentoDen;
    }
}

void checandoAbsurdos(int numEquacoes, coeficiente **matAlocada, int lin){
    
    //  Função utilizada para a checagem de absurdos nas equações da matriz.

    int a, b, c, d;

    if(matAlocada[lin][0].denominador == 0){
        a = 0;
    }
    else{
        a = matAlocada[lin][0].numerador / matAlocada[lin][0].denominador;
    }

    if(matAlocada[lin][1].denominador == 0){
        b = 0;
    }
    else{
        b = matAlocada[lin][1].numerador / matAlocada[lin][1].denominador;
    }

    if(matAlocada[lin][2].denominador == 0){
        c = 0;
    }
    else{
        c = matAlocada[lin][2].numerador / matAlocada[lin][2].denominador;
    }

    if(matAlocada[lin][3].denominador == 0){
        d = 0;
    }
    else{
        d = matAlocada[lin][3].numerador / matAlocada[lin][3].denominador;
    }

    if(a == 0 && b == 0 && c == 0 && d != 0){ // Significa que existe um absurdo. Portanto, não há colisão.
        achouAbsurdo = true;
    }
    else{ // Não há absurdo. 
        achouAbsurdo = false;
    }
}

void algoritmoEscalonamento(int numEquacoes, int numCoeficientes, coeficiente** matAlocada, int contador, int lin, int col){
    
    // Esse algoritmo, chamado de Eliminação Gaussiana, é utilizado para resolução de equações
    // lineares de forma simplificada. Nessa função, iremos checar as condições necessárias
    // para a implementação do algoritmo e, então, implementá-lo.

    contador = 0;
    if((double) matAlocada[lin-1][col].numerador / (double) matAlocada[lin-1][col].denominador == 0) {
        contador = coeficientePositivo(matAlocada, lin, col, numEquacoes); // A primeira condição é o primeiro coeficiente da equação ser não nulo
        swap(matAlocada, contador, numCoeficientes, lin); // Se ele não for, precisaremos escalonar a matriz
    }

    coeficiente pivo, x;
    pivo.numerador = matAlocada[lin-1][col].numerador;
    pivo.denominador = matAlocada[lin-1][col].denominador;

    // A seguir, será implementada uma equação para o algoritmo de escalonamento. Foi realizado o MMC nessa equação para facilitar os cálculos.
    for(int i = lin; i < numEquacoes; i++){    
        x.numerador = matAlocada[i][col].numerador;
        x.denominador = matAlocada[i][col].denominador;

        for(int j = col; j < 4; j++){
            matAlocada[i][j].numerador = (matAlocada[lin-1][j].denominador * x.denominador * pivo.numerador * matAlocada[i][j].numerador) - (matAlocada[i][j].denominador * matAlocada[lin-1][j].numerador * x.numerador * pivo.denominador);
            matAlocada[i][j].denominador = matAlocada[i][j].denominador * matAlocada[lin-1][j].denominador * x.denominador * pivo.numerador;
            checandoAbsurdos(numEquacoes, matAlocada, i);
        }
    }

    // Precisamos verificar a todo o momento, pelo fato da função ser recursiva, se a quantidade de linhas
    // recebidas é menor que a quantidade total de equações. Se não, o programa pode apresentar erro.
    if(lin+1 < numEquacoes){
        lin++, col++;
        algoritmoEscalonamento(numEquacoes, numCoeficientes, matAlocada, contador, lin, col);
    }
}

void liberacaoMemoria(int numCoeficientes, coeficiente** matAlocada, int numEquacoes){

    for(int i = 0; i < numEquacoes; i++){
        free(matAlocada[i]);
    }
    free(matAlocada);
}

int main(int argc, char const *argv[]){

    int numEquacoes, numCoeficientes, posicao = 0, contador = 0, lin = 1, col = 0;
    scanf("%d%d", &numEquacoes, &numCoeficientes);

    coeficiente **matAlocada;
    matAlocada = alocacaoMatriz(numEquacoes, numCoeficientes);
    
    char objeto1, objeto2;
    scanf(" %c", &objeto1);
	posicao = leituraEquacoes(objeto1, numEquacoes, matAlocada, posicao);
	
    scanf(" %c", &objeto2);
    posicao = leituraEquacoes(objeto2, numEquacoes, matAlocada, posicao);
    
    algoritmoEscalonamento(numEquacoes, numCoeficientes, matAlocada, contador, lin, col);

    printaMatriz(matAlocada, numEquacoes, achouAbsurdo);

    liberacaoMemoria(numCoeficientes, matAlocada, numEquacoes);
    
    return 0;
}
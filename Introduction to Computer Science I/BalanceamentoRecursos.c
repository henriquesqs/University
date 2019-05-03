/*
 Programa de checagem de balanceamento de recursos. O objetivo desse programa é verificar se algum jogador
 possui vantagem sobre o outro no que diz respeito à distâcia entre sua base e um recurso.
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
#include <stdbool.h>
#include <math.h>
#include <stdlib.h>

bool AchouRecurso = false;

int **AlocacaoRecursos(int nRec)
{

    /*
    Nessa função, as coordenadas dos recursos serão alocados na memória heap para que não sejam perdidas
    durante a execução do programa. Assim, poderemos facilmente acessar essas coordenadas durante toda
    a execução desse codigo.
    */

    int **posRec = (int **)malloc(nRec * (sizeof(int *))); // alocando o numero de linhas da matriz

    for (int k = 0; k < nRec; k++)
    {
        posRec[k] = (int *)malloc(2 * (sizeof(int))); // alocando o numero de colunas da matriz
    }

    for (int j = 0; j < nRec; j++)
    {
        scanf("%d%d", &posRec[j][0], &posRec[j][1]); // lendo o numero de recursos
    }

    return posRec;
}

int Contador(int map[9][9], int contador)
{
    /*
    Contagem de quantos espaços o algoritmo percorreu até encontrar o recurso.
    Esse contador será utilizado posteriormente para verificar se existe algum
    jogador que possui vantagem sobre o outro.
    */

    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            if (map[i][j] == 3 || map[i][j] == 2)
            {
                contador++;
                map[i][j] = 0;
            }
        }
    }

    return contador;
}

void floodFill(int map[9][9], int posL, int posC)
{
    /*
    O algoritmo de preenchimento, floodFill, irá percorrer o mapa em busca do recurso (declarado nesse código como o número 3).
    Partindo da base do jogador, ele irá calcular a distância dessa base ao local do recurso e modificar os espaços que
    percorreu, isto é, os transponíveis, para 2. Entretando, isso só ocorrerá até que o algoritmo encontre o recurso.
    */

    if (posL >= 9 || posL < 0 || posC >= 9 || posC < 0)
    { // Caso o algoritmo ultrapasse o tamanho do mapa, retornar
        return;
    }

    if (map[posL][posC] == 3)
    { // Se a posição no mapa for igual a 3, achamos o recurso
        AchouRecurso = true;
        return;
    }

    if (map[posL][posC] == 0 && !AchouRecurso)
    {
        map[posL][posC] = 2;
        floodFill(map, posL + 1, posC); // sul
        floodFill(map, posL - 1, posC); // norte
        floodFill(map, posL, posC - 1); // oeste
        floodFill(map, posL, posC + 1); // leste
    }
}

float modificacaoMatriz(int **posRec, int nRec, int map[9][9], int posL, int posC, int contador)
{

    /*
    Nessa função, o mapa irá receber o recurso. Basicamente, iremos pegar as coordenadas do recurso
    e, no mapa, declarar esse ou mais recursos como o número '3'. Isso facilitará na busca pelo mesmo
    durante a utilização do algoritmo de preenchimento.
    */

    int linRec, colRec;
    float E = 0;

    for (int k = 0; k < nRec; k++)
    {
        linRec = posRec[k][0]; // Declarando a linha que recebe o recurso
        colRec = posRec[k][1]; // Declarando a coluna que recebe o recurso

        map[linRec][colRec] = 3;

        floodFill(map, posL, posC);

        AchouRecurso = false;
        E += Contador(map, contador);
    }

    return E;
}

void calculoVantagem(int p, int nRec, int **posRec, int map[9][9], int pos1L, int pos1C, int pos2L, int pos2C)
{

    /*
    Essa função irá realizar o objetivo do trabalho: checar se há algum jogador que possui vantagem sobre outro
    baseado na distância entre as bases desses jogadores e os recursos existentes. Se um jogador (A) estiver menos 
    distante de um recurso do que outro jogador (B), então o jogador (A) possui vantagem sobre o (B). Para tudo isso,
    algumas funções irão realizar modificações no mapa para que essa checagem seja possível.
    */

    int contador = 0;
    float jogadorUm, jogadorDois;

    jogadorUm = modificacaoMatriz(posRec, nRec, map, pos1L, pos1C, contador);

    jogadorDois = modificacaoMatriz(posRec, nRec, map, pos2L, pos2C, contador);

    float E1, E2;

    E1 = (1 / (double)nRec) * (jogadorUm / p);

    E2 = (1 / (double)nRec) * (jogadorDois / p);

    if (fabs(E1 - E2) < 0.001)
    {
        printf("%lf\n%lf\nO mapa eh balanceado", E1, E2);
    }

    if (E1 > E2)
    {
        printf("%lf\n%lf\nO jogador 2 possui vantagem", E1, E2);
    }
    if (E2 > E1)
    {

        printf("%lf\n%lf\nO jogador 1 possui vantagem", E1, E2);
    }
}

void desalocaMatriz(int **posRec, int nRec)
{

    /*
    Realizado todo o trabalho, precisamos devolver a memória que reservamos para que não
    haja o vazamento de memória, isto é, para que não existam pedaços de memórias perdidos
    e inacessíveis até que a máquina seja reiniciada.
    */

    for (int i = 0; i < nRec; i++)
    {
        free(posRec[i]);
    }
    free(posRec);
}

int main(int argc, char const *argv[])
{

    /*  
    O bloco lógico ("for") a seguir irá percorrer e preencher a matriz com os valores 
    '0' e '1' recebidos na entrada, isto é, locais do mapa que
    são acessíveis ou não para o usuário.
    */

    int map[9][9], p = 0; // O inteiro 'p' irá armazenar a quantidade de espaços transponíveis

    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            scanf("%d", &map[i][j]);
            if (map[i][j] == 0)
            {
                p++;
            }
        }
    }

    int pos1L, pos1C, pos2L, pos2C; // Declaração e posterior leitura das posições LC (linha/coluna) de cada jogador
    scanf("%d%d%d%d", &pos1L, &pos1C, &pos2L, &pos2C);

    /*
    A seguir, precisamos receber as posições 'x' e 'y' no mapa de cada recurso existente.
    Para isso, irei criar uma matriz nRec*2 para alocar na heap as posições de maneira que me 
    permita utilizá-las facilmente e sem que eu as perca.
    */

    int nRec; // 'nRec' é o número total de recursos
    scanf("%d", &nRec);

    int **posRec; // 'posRec' é o conjunto de coordenadas de cada um

    posRec = AlocacaoRecursos(nRec);

    calculoVantagem(p, nRec, posRec, map, pos1L, pos1C, pos2L, pos2C);

    desalocaMatriz(posRec, nRec);

    return 0;
}

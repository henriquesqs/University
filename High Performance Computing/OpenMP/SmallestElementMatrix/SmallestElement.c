/*
    Gustavo T. Mastrobuono, NUSP 10734411;
    Henrique de S. Q. dos Santos, NUSP 10819029;
    Jhordan P. V. Pesantes, NUSP 11733353;
    Witor M. A. de Oliveira, NUSP 10692190;
    Yorvin A. R. Carrion, NUSP 11733332;
*/

#include <stdio.h>
#include <omp.h>
#include <stdlib.h>

// valor maximo na matriz. Se a matriz tiver valores que 
// ultrapassam as 6 casas, aumentar esse valor também
#define MAX_VALUE 999999

int main(){

    omp_set_nested(1); // permitindo o uso de paralelismos aninhados
    
    int **mat, i = 0, j = 0, n = 0, pos = 0;
    int menorLocal = MAX_VALUE, menorGlobal = MAX_VALUE;

    // tamanho da matriz e posição nela
    scanf("%d\n%d\n", &n, &pos);

    // Alocação de memória para a matriz
    mat = (int**) malloc(n * sizeof(int*));

    for(int j = 0; j < n; j++)
        mat[j] = (int*) malloc(n * sizeof(int));

    // Lendo valores e armazenando na matriz
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
           scanf("%d", &mat[i][j]);
    
    // Esse vetor armazenará o maior valor encontrado 
    // para cada linha da matriz. Aqui alocamos memória
    // para ele e o inicializamos
    int *vet = (int *) malloc(n * sizeof(int));
    
    for(i = 0; i < n; i++)
        vet[i] = MAX_VALUE;
    
    // Criando uma região paralela que irá criar N threads
    // uma thread para cada linha. Para cada uma dessas threads
    // serão geradas mais N/T threads que ficarão responsáveis
    // por verificar a existência de um menor maior valor
    // nas N/T partes da linha que ficou responsável.
    // O OMP define automaticamente o numero T de threads.
    #pragma omp parallel for shared(vet) schedule(static, n)
        for(i = 0; i < n; i++){
            #pragma omp parallel for firstprivate(menorLocal, pos) shared(vet) 
                for(j = 0; j < n; j++){
                    if((mat[i][j] > mat[i][pos]) && (mat[i][j] < menorLocal))
                        menorLocal = mat[i][j];

                    #pragma omp critical
                        if(menorLocal < vet[i])
                            vet[i] = menorLocal;
                }
        }

    for (i = 0; i < n; i++){
        if(vet[i] == MAX_VALUE)
            printf("-1 ");
        else
            printf("%d ", vet[i]);
    }
    printf("\n");

    // Liberando memória alocada para matriz
    for(i = 0; i< n; i++)
        free(mat[i]);

    free(mat);

    // Liberando memória alocada para vetor 
    // com os menores maiores valores de cada linha
    free(vet);

    return 0;
    
}
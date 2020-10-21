#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <string.h>

#define T 4

int main(){
    
    omp_lock_t lock;
    omp_init_lock(&lock); // inicializando nosso lock
    
    int numCaracteres = 0;
    scanf("%d\n", &numCaracteres);

    char text[numCaracteres];
    
    // Leitura da palavra e alocação em um vetor
    for(int i = 0; i < numCaracteres; i++){
        scanf("%c", &text[i]);
    }

    int i = 0;
    int numPalavras = 100; // definindo um tamanho máximo de palavras
    char **matrix = (char**)malloc(sizeof(char*)*numPalavras);
    
    char *token = strtok(text, " \n"); // definindo a variavel que armazenara cada palavra

    while(token != NULL) {
        matrix[i] = (char*)malloc(sizeof(char)*strlen(token+1));
        strcpy(matrix[i], token);
        token = strtok(NULL," \n");
        i++;
    }
    numPalavras = i;
    
    int maiorLocal = 0, maiorGlobal = 0;

    #pragma omp parallel num_threads(numPalavras) private(maiorLocal, token) shared(maiorGlobal)
    {
    
        // Percorre a matriz de palavras contando o tamanho de cada uma
        maiorLocal = strlen(matrix[omp_get_thread_num()]);

        // Região crítica, compara se o maior valor encontrado localmente é o maior global
        omp_set_lock(&lock);
        if(maiorLocal > maiorGlobal){
            maiorGlobal = maiorLocal;
        }
        omp_unset_lock(&lock);
    }

    printf("Tamanho da maior palavra: %d\n", maiorGlobal);
    
    // Desalocando memória da matriz
    for (int i = 0; i < numPalavras; i++){
        free(matrix[i]);
    }

    free(matrix);

    return 0;
    
}
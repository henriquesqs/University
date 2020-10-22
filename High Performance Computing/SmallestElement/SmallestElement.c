// Gustavo T. Mastrobuono NUSP 10734411, Henrique de S. Q. dos Santos NUSP 10819029, 
// Jhordan P. V. Pesantes NUSP 11733353, Witor M. A. de Oliveira NUSP 10692190 e Yorvin A. R. Carrion NUSP 11733332

#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <string.h>

#define T 4 // numero de threads

int main(){
    
    omp_lock_t lock;
    omp_init_lock(&lock); // inicializando nosso lock
    
    int i = 0, n = 0, pos = 0, comparador = 0, menorLocal, iteracoes = 0, menorGlobal = 0, resto = 0;

    scanf("%d", &n); // tamanho do vetor
    scanf("%d", &pos); // posição do vetor

    int vet[n], vetor_resto[T] = {0};

    for(int i = 0; i < n; i++){
        scanf("%d", &vet[i]); // lendo valores do vetor
    }    	

    comparador = vet[pos]; // salvando o valor a ser comparado
    iteracoes = n / T; // limite de iteracoes de cada tarefa
    resto = n%T; // verificando se é possivel efetuar uma divisao exata dos dados

    for(i = 0; i < resto; i++) // inicializando o vetor de resto 
		vetor_resto[i] = 1; // ele armazena se a thread precisa fazer mais iterações

    menorGlobal = 99999;

    #pragma omp parallel num_threads(T) private(i) shared(menorGlobal)
    {   

        // inicializando variaveis para cada processo
        int menorLocal = 99999;
        
        // Esse laço efetua a divisão exata de dados entre os processos disponíveis
        for (i = omp_get_thread_num() * iteracoes; i < iteracoes + omp_get_thread_num() * iteracoes; i++) {	
            
            if((vet[i] > comparador) && (vet[i] < menorLocal)){
                menorLocal = vet[i];
            }
        }

        // verifica se a thread precisa fazer operação a mais para suprir o resto do vetor
        if(vetor_resto[omp_get_thread_num()] == 1){ 
            if((vet[iteracoes*T + omp_get_thread_num()] > comparador) && (vet[iteracoes*T + omp_get_thread_num()] < menorLocal)){
                menorLocal = vet[iteracoes*T + omp_get_thread_num()];
            }
        }

        // Após a computação do menor local no bloco recebido pelo processo,
        // efetua a comparação com o menor global
        omp_set_lock(&lock);
        if(menorLocal < menorGlobal){
            menorGlobal = menorLocal;
        }
        omp_unset_lock(&lock);
    }
    
    if(menorGlobal == 99999)
        printf("-1");
    else printf("%d\n", menorGlobal);
    
    return 0;
    
}